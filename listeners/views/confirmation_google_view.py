from logging import Logger
from slack_bolt import Ack
from slack_sdk import WebClient


def confirmation_google_view_callback(ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()
        user_id = body["user"]["id"]
        channel_id  = body["user"]["id"]


        client.chat_postEphemeral(
            channel=channel_id,
            user=user_id,
            text="Le formulaire a été transmis avec succès"
        )
    except Exception as e:
        logger.error(e)
