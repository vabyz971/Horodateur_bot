from slack_bolt import Ack, Respond
from logging import Logger
from models.user import User


def add_user_callback(command, ack: Ack, respond: Respond, logger: Logger):
    try:
        ack()
        
        arguments : list[str] = command["text"].split("|")
        logger.info(arguments)
        user = User(arguments[0], arguments[1], arguments[2]).save()
        if(user):
            print("User saved successfully!")
            respond("User saved successfully !")
        else:
            print("Error while saving the user.")
            respond("Error while saving the user.")
        
    except Exception as e:
        logger.error(e)
