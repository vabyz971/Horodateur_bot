import os
import requests
from logging import Logger
from slack_bolt import Ack
from slack_sdk import WebClient
from sqlalchemy.orm import Session
from database import EngineDatabase
from models.User import UserModel


engine = EngineDatabase.start_engine()


def user_exist(user_id: str):
    with Session(engine) as session:
        user = session.query(UserModel).filter(UserModel.id_slack == user_id).first()
        if user is not None:
            return user
        else:
            return False


def validation_form(data: dict):
    if (
        data["horodateur"]
        and data["periode"]
        and data["presence"]
        and data["competence"]
    ):
        return True
    return False


def send_request_google_forms(form: dict, logger: Logger):
    FORM_ID = os.environ.get("GOOGLE_FORM_ID")
    ENTRY_ID = {
        "username": os.environ.get("GOOGLE_FORM_INPUT_NAME"),
        "horodateur": os.environ.get("GOOGLE_FORM_INPUT_HORODATEUR"),
        "periode": os.environ.get("GOOGLE_FORM_INPUT_PERIODE"),
        "presence": os.environ.get("GOOGLE_FORM_INPUT_PRESENCE"),
        "competence": os.environ.get("GOOGLE_FORM_INPUT_COMPETENCE"),
        "note": os.environ.get("GOOGLE_FORM_INPUT_NOTE"),
    }
    # URL de soumission Google Forms
    SUBMIT_URL = f"https://docs.google.com/forms/d/e/{FORM_ID}/formResponse"

    payload = {
        ENTRY_ID["username"]: form["user"],
        ENTRY_ID["horodateur"]: form["horodateur"],
        ENTRY_ID["periode"]: form["periode"],
        ENTRY_ID["presence"]: form["presence"],
        ENTRY_ID["competence"]: form["competence"],
        ENTRY_ID["note"]: form["note"],
    }

    # Headers pour simuler un navigateur
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Referer": SUBMIT_URL,
    }

    try:
        response = requests.post(SUBMIT_URL, data=payload, headers=headers)
        response.raise_for_status()

        # Vérification de la soumission réussie (le contenu peut varier)
        if response.status_code == int(200):
            print("✅ Soumission réussie !")
            return True
        else:
            print("⚠️ Réponse inattendue - vérifiez le formulaire")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la soumission: {e}")
        return False


def submit_horodateur_action_callback(
    ack: Ack, client: WebClient, body: dict, logger: Logger
):
    try:
        ack()

        # `submit_form_data = body["view"]["state"]["values"]` is extracting the values of the form
        submit_form_data = body["view"]["state"]["values"]

        form_horodateur = submit_form_data["form_horodateur"]["form.horodateur"][
            "selected_option"
        ]["value"]
        form_periode = submit_form_data["form_periode"]["form.periode"][
            "selected_option"
        ]["value"]
        form_presence = submit_form_data["form_presence"]["form.presence"][
            "selected_option"
        ]["value"]
        form_competence = submit_form_data["form_competence"]["form.competence"][
            "selected_option"
        ]["value"]
        form_note = submit_form_data["form_note"]["form.note"]["value"] or ""


        model_form_data = {
            "user": user_exist(body["user"]["id"]).name,
            "horodateur": form_horodateur,
            "periode": form_periode,
            "presence": form_presence,
            "competence": form_competence,
            "note": form_note,
        }

        print(model_form_data["user"])

        if validation_form(model_form_data):
            if send_request_google_forms(model_form_data, logger):
                client.views_open(
                    trigger_id=body["trigger_id"],
                    view={
                        "type": "modal",
                        "callback_id": "confirmation_google_view",
                        "submit": {
                            "type": "plain_text",
                            "text": "Ok",
                            "emoji": True,
                        },
                        "close": {
                            "type": "plain_text",
                            "text": "Fermer",
                            "emoji": True,
                        },
                        "title": {
                            "type": "plain_text",
                            "text": "Formulaire valider",
                            "emoji": True,
                        },
                        "blocks": [
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": f"Horodateur vous enverra une confirmation par message.",
                                },
                            }
                        ],
                    },
                )

    except Exception as e:
        logger.error(e)
