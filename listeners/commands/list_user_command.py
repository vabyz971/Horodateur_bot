from slack_bolt import Ack, Respond
from logging import Logger
from sqlalchemy.orm import Session
from database import EngineDatabase
from models.User import UserModel


engine = EngineDatabase.start_engine()

session = Session(bind=engine)


def list_user_section():
    items = []
    with Session(engine) as session:
        users = session.query(UserModel).all()
        if users is not None:
            for user in users:
                items.append(
                    {
                        "type": "rich_text_section",
                        "elements": [{"type": "text", "text": f"<@{user.name}>"}],
                    },
                )
                print(user.id_slack + " : " + user.name)
        else:
            items.append(
                {
                    "type": "rich_text_section",
                    "elements": [
                        {"type": "text", "text": "Aucun utilisateur n'est enregistré."}
                    ],
                },
            )

    return items


def list_user_callback(command, ack: Ack, respond: Respond, logger: Logger):
    HEADER_BLOCK = {
        "type": "header",
        "text": {"type": "plain_text", "text": "Liste des utilisateurs", "emoji": True},
    }

    DIVIDER_BLOCK = {"type": "divider"}
    LIST_USERS = {
        "type": "rich_text",
        "elements": [
            {"type": "rich_text_section", "elements": [{"type": "text", "text": "..."}]},
            {
                "type": "rich_text_list",
                "style": "bullet",
                "indent": 0,
                "elements": list_user_section(),
            },
        ],
    }
    
    _blosk = [HEADER_BLOCK, DIVIDER_BLOCK, LIST_USERS, DIVIDER_BLOCK]
    
    print(_blosk)
    
    try:
        ack()
        respond(
            blocks=_blosk,
        )

    except Exception as e:
        logger.error(e)
