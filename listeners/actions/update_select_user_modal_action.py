from logging import Logger
from ..utils.verifications import is_user_admin
from slack_bolt import Ack
from slack_sdk import WebClient


def update_select_user_modal_action_callback(
    ack: Ack, client: WebClient, body: dict, logger: Logger
):
    ## VIEW MODAL BLOCK

    DESCRIPTION_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Ajouter un utilisateur pour qu'il soit automatiquement redirigé sur le bon formulaire",
        },
    }

    modal_values = body["view"]["state"]["values"]
    select_user_id = modal_values["list_user_id"]["update_select_user_modal_action"][
        "selected_user"
    ]

    LIST_USERS_BLOCK = {
        "type": "section",
        "block_id": "list_user_id",
        "text": {
            "type": "mrkdwn",
            "text": f"Utilisateur sélectionné : <@{select_user_id}>",
        },
        "accessory": {
            "type": "users_select",
            "placeholder": {
                "type": "plain_text",
                "text": "Liste des utilisateurs",
                "emoji": True,
            },
            "action_id": "update_select_user_modal_action",
        },
    }

    NAME_USER_BLOCK = {
        "type": "input",
        "block_id": "name_user_id",
        "element": {"type": "plain_text_input", "action_id": "name_user"},
        "label": {
            "type": "plain_text",
            "text": "Nom du nouvel utilisateur : ",
            "emoji": True,
        },
    }

    LIST_GROUPS_BLOCK = {
        "type": "input",
        "block_id": "group_user_id",
        "element": {
            "type": "static_select",
            "placeholder": {
                "type": "plain_text",
                "text": "Sélectionner un groupe",
                "emoji": True,
            },
            "options": [
                {
                    "text": {
                        "type": "plain_text",
                        "text": "Groupe J01",
                        "emoji": True,
                    },
                    "value": "J01",
                },
                {
                    "text": {
                        "type": "plain_text",
                        "text": "Groupe H01",
                        "emoji": True,
                    },
                    "value": "H01",
                },
            ],
            "action_id": "group_user",
        },
        "label": {"type": "plain_text", "text": "List des groupes", "emoji": True},
    }

    try:
        ack()
        ## IS USER AN ADMIN
        if is_user_admin(body["user"]["id"]):
            client.views_update(
                view_id=body["view"]["id"],
                hash=body["view"]["hash"],
                view={
                    "type": "modal",
                    "callback_id": "add_user_view",
                    "title": {
                        "type": "plain_text",
                        "text": "Ajouter un utilisateur",
                    },
                    "blocks": [
                        DESCRIPTION_BLOCK,
                        LIST_USERS_BLOCK,
                        NAME_USER_BLOCK,
                        LIST_GROUPS_BLOCK,
                    ],
                    "submit": {
                        "type": "plain_text",
                        "text": "Ajouter",
                        "emoji": True,
                    },
                    "close": {"type": "plain_text", "text": "Fermer", "emoji": True},
                },
            )

        else:
            return client.chat_postMessage(
                channel=body["channel_id"], text="Vous n'êtes pas Admin !!!"
            )

    except Exception as e:
        logger.error(e)
