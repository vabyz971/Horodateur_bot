from slack_bolt import Ack, Respond
from logging import Logger
from slack_sdk import WebClient
from ..utils.verifications import is_user_admin
from ..utils.elements_blocks import section, list_users_block_slack, input_text, input_select


def add_user_callback(
    body, ack: Ack, client: WebClient, respond: Respond, logger: Logger
):
    # VIEW MODAL BLOCK
    BLOCK = [
        section("Ajouter un utilisateur pour qu'il soit automatiquement redirigé sur le bon formulaire"),
        list_users_block_slack(
            title="Sélectionnez un utilisateur",
            placeholder="Liste des utilisateurs",
            action_id="update_select_user_modal_action",
            block_id="list_user_id"),
        input_text(
            label="Nom du nouvel utilisateur : ",
            action_id="name_user",
            block_id="name_user_id"
        ),
        input_select(
            label="List des groupes",
            placeholder="Sélectionner un groupe",
            action_id="group_user",
            block_id="group_user_id",
            options={
                "Groupe J01": "J01",
                "Groupe H01": "H01"}
        )
    ]

    try:
        ack()

        # IS USER AN ADMIN
        if is_user_admin(body["user_id"]):
            client.views_open(
                trigger_id=body["trigger_id"],
                view={
                    "type": "modal",
                    "callback_id": "add_user_view",
                    "title": {"type": "plain_text", "text": "Ajout d'un utilisateur"},
                    "blocks": BLOCK,
                    "submit": {
                            "type": "plain_text",
                            "text": "Ajouter",
                            "emoji": True,
                    },
                    "close": {"type": "plain_text", "text": "Fermer", "emoji": True},
                },
            )
        else:
            return respond("Vous n'êtes pas Admin !!!")

    except Exception as e:
        logger.error(e)
