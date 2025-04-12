from logging import Logger
from slack_bolt import Ack, Respond
from ..utils.elements_blocks import header, section_list


def infos_command_callback(ack: Ack, respond: Respond, logger: Logger):
    try:
        ack()

        BLOCK = [
            header("Information :spiral_note_pad:"),
            section_list([
                '*Description* :\n Bot Slack qui simplifie l\'horodatage avec quelques fonctionnalités plutôt sympa.\
                 Crée par et pour les élèves d\'infographies de Bel-Avenir',
                '*Auteur* : vabyz971',
                '*Version* : 0.1.0',
            ])
        ]

        respond(blocks=BLOCK)
    except Exception as e:
        logger.error(e)
