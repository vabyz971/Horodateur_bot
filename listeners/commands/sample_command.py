from slack_bolt import Ack, Respond
from logging import Logger

def sample_command_callback(command, ack: Ack, respond: Respond, logger: Logger):
    try:
        ack()
        respond("Sample command received. This is the response to your command.")

    except Exception as e:
        logger.error(e)
