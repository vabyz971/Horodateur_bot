from models.User import UserModel


def header(text: str):
    return {
        "type": "header",
        "text": {"type": "plain_text", "text": text, "emoji": True},
    }


def section(text: str):
    return {
        "type": "section",
        "text": {"type": "mrkdwn", "text": text},
    }


def tab_rich_text(elements: list, title: str):
    items = []
    for index, element in elements:
        items.append(
            {
                "type": "rich_text_section",
                "elements": [{"type": "text", "text": f"{index} -|- {element}"}],
            }
        )

    return {
        "type": "rich_text",
        "elements": [
            {
                "type": "rich_text_section",
                "elements": [{"type": "text", "text": title, "emoji": True}],
            },
            {
                "type": "rich_text_section",
                "style": "bullet",
                "indent": 0,
                "elements": items,
            },
        ],
    }


def list_users_section(users: list[UserModel]):  
    items = []
    for user in users:
        items.append(
            section(f"{user.id} | *<@{user.id_slack}>* | {user.name} - {user.groupe}")
        )
    return items


def context(elements: list):
    items = []
    for element in elements:
        items.append(
            {
                "type": "mrkdwn",
                "text": element,
            }
        )
    return {
        "type": "context",
        "elements": items,
    }


def accessory(blocks):
    return {
        "accessory" : {
            blocks
        }
    }


def button(name : str, style : str ,action: str = "action_id", value : str = ""):
    return{
        "type": "button",
        "text":{
            "type":"plain_text",
            "emoji":True,
            "text":name
        },
        "value": value,
        "style": style,
        "action_id": action,
    }


def divider():
    return {"type": "divider"}
