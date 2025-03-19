from slack_bolt import Ack, Respond
from logging import Logger
from models.user import User


def list_user_callback(command, ack: Ack, respond: Respond, logger: Logger):
    try:
        ack()
        lists_user = User.get_all()
        for user in lists_user:
            respond(f"List of users : {user}")
        
    except Exception as e:
        logger.error(e)
