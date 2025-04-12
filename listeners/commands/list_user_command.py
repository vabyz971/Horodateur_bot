from slack_bolt import Ack, Respond
from logging import Logger
from slack_sdk import WebClient
from ..utils.verifications import is_user_admin
from ..utils.elements_blocks import divider, context, list_users_section
from sqlalchemy.orm import Session
from database import EngineDatabase
from models.User import UserModel


def list_user_callback(
    body: dict, client: WebClient, ack: Ack, respond: Respond, logger: Logger
):

    BLOCKS = [
        divider(),
        *list_users_section(UserModel.get_all()),
        divider(),
        context(["Nombre d'utilisateurs : " + str(UserModel.count())]),
    ]

    try:
        ack()

        if is_user_admin(body["user_id"]):
            client.views_open(
                trigger_id=body["trigger_id"],
                view={
                    "type": "modal",
                    "title": {"type": "plain_text", "text": "Liste des utilisateurs"},
                    "blocks": BLOCKS,
                    "close": {"type": "plain_text", "text": "Fermer", "emoji": True},
                },
            )

        else:
            return respond("Vous n'êtes pas Admin  !!!")

    except Exception as e:
        logger.error(e)
