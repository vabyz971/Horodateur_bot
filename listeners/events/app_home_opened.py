from logging import Logger
from slack_sdk import WebClient


def app_home_opened_callback(client: WebClient, event: dict, logger: Logger):
    # ignore the app_home_opened event for anything but the Home tab
    if event["tab"] != "home":
        return
    try:
        HEADER_BLOCK = {
            "type": "header",
            "text": {"type": "plain_text", "text": "Horodateur", "emoji": True},
        }


        SECTION_BLOCK = {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Indiquez votre présence à tous les cours (période de 3 heures)",
                "emoji": True,
            },
        }

        DIVIDER_BLOCK = {"type": "divider"}

        HEADER_FORM_BLOCK = {
            "type": "header",
            "text": {"type": "plain_text", "text": "Formulaire", "emoji": True},
        }

        RADIO_HORODATEUR_INPUT_BLOCK = {
            "type": "input",
            "block_id": "form_horodateur",
            "element": {
                "type": "radio_buttons",
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Arrivée",
                            "emoji": True,
                        },
                        "value": "Arrivée",
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Départ hâtif",
                            "emoji": True,
                        },
                        "value": "Départ hâtif",
                    },
                ],
                "action_id": "form.horodateur",
            },
            "label": {
                "type": "plain_text",
                "text": "Horodateur",
                "emoji": True,
            },
        }

        RADIO_PERIODE_INPUT_BLOCK = {
            "type": "input",
            "block_id": "form_periode",
            "element": {
                "type": "radio_buttons",
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "AM :clock8: ",
                            "emoji": True,
                        },
                        "value": "AM",
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PM :clock130: ",
                            "emoji": True,
                        },
                        "value": "PM",
                    },
                ],
                "action_id": "form.periode",
            },
            "label": {
                "type": "plain_text",
                "text": "Période",
                "emoji": True,
            },
        }

        RADIO_PRESENCE_INPUT_BLOCK = {
            "type": "input",
            "block_id": "form_presence",
            "element": {
                "type": "radio_buttons",
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "En classe",
                            "emoji": True,
                        },
                        "value": "En classe",
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "À distance",
                            "emoji": True,
                        },
                        "value": "À distance",
                    },
                ],
                "action_id": "form.presence",
            },
            "label": {
                "type": "plain_text",
                "text": "Présence",
                "emoji": True,
            },
        }

        RADIO_COMPETENCE_INPUT_BLOCK = {
            "type": "input",
            "block_id": "form_competence",
            "element": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Sélectionner une compétence",
                    "emoji": True,
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Compétence 1",
                            "emoji": True,
                        },
                        "value": "Compétence 1",
                    }
                ],
                "action_id": "form.competence",
            },
            "label": {
                "type": "plain_text",
                "text": "Compétence travaillée durant la période",
                "emoji": True,
            },
        }

        HEADER_NOTE_FORM_BLOCK = {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "As-tu quelque chose à ajouter ?",
                "emoji": True,
            },
        }

        SECTION_NOTE_FORM_BLOCK = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Du genre, « ouin, j'avais oublié de puncher en arrivant mais je suis arrivé à 8h30 », ou bien « je vais devoir quitter entre 10h et 10h30 à cause d'un rendez-vous chez le blablabla... ». Tu vois le genre?",
            },
        }

        INPUT_NOTE_FORM_BLOCK = {
            "type": "input",
            "block_id": "form_note",
            "element": {"type": "plain_text_input", "action_id": "form.note"},
            "label": {
                "type": "plain_text",
                "text": "Tu peux l'écrire ici dans la section Note. ",
                "emoji": True,
            },
        }

        BUTTON_SUBMIT_FORM_BLOCK = {
            "type": "actions",
            "block_id": "form_submit",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Valider",
                        "emoji": True,
                    },
                    "value": "submit",
                    "action_id": "form.submit",
                },
            ],
        }

        client.views_publish(
            user_id=event["user"],
            view={
                "type": "home",
                "blocks": [
                    HEADER_BLOCK,
                    SECTION_BLOCK,
                    DIVIDER_BLOCK,
                    HEADER_FORM_BLOCK,
                    RADIO_HORODATEUR_INPUT_BLOCK,
                    DIVIDER_BLOCK,
                    RADIO_PERIODE_INPUT_BLOCK,
                    DIVIDER_BLOCK,
                    RADIO_PRESENCE_INPUT_BLOCK,
                    DIVIDER_BLOCK,
                    RADIO_COMPETENCE_INPUT_BLOCK,
                    DIVIDER_BLOCK,
                    HEADER_NOTE_FORM_BLOCK,
                    SECTION_NOTE_FORM_BLOCK,
                    INPUT_NOTE_FORM_BLOCK,
                    BUTTON_SUBMIT_FORM_BLOCK,
                ],
            },
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
