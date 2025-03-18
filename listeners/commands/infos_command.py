from logging import Logger
from slack_bolt import Ack, Respond


def infos_command_callback(ack: Ack, respond: Respond, logger: Logger):
    try:
        ack()
        HEADER_BLOCK = {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Information :spiral_note_pad:",
                "emoji": True,
            },
        }
        LIST_BLOCK = [
            {
                "type": "rich_text_section",
                "elements": [
                    {"type": "text", "text": "Nom: "},
                    {
                        "type": "text",
                        "text": "@Horodateur",
                    },
                ],
            },
            {
                "type": "rich_text_section",
                "elements": [
                    {"type": "text", "text": "Version: "},
                    {
                        "type": "text",
                        "text": "0.2.0",
                    },
                ],
            },
            {
                "type": "rich_text_section",
                "elements": [
                    {"type": "text", "text": "Autheur: "},
                    {
                        "type": "link",
                        "url": "https://github.com/vabyz971",
                        "text": "Vabyz971",
                        "style": {
                            "bold": True,
                        },
                    },
                ],
            },
        ]

        SECTION_BLOCK = {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_section",
                    "elements": [
                        {
                            "type": "text",
                            "text": "Details: ",
                        }
                    ],
                },
                {
                    "type": "rich_text_list",
                    "style": "bullet",
                    "indent": 0,
                    "elements": LIST_BLOCK,
                },
            ],
        }
        respond(blocks=[HEADER_BLOCK, SECTION_BLOCK])
    except Exception as e:
        logger.error(e)
