from models.User import UserModel


def header(text: str):
    return {
        "type": "header",
        "text": {"type": "plain_text", "text": text, "emoji": True},
    }


def section(text: str, block_id: str = ""):
    return {
        "type": "section",
        "block_id": block_id,
        "text": {"type": "mrkdwn", "text": text},
    }


def section_accessory(text: str, block_id: str = "", accessory: str = ""):
    return {
        "type": "section",
        "block_id": block_id,
        "text": {
            "type": "mrkdwn",
            "text": text,
        },
        "accessory": accessory
    }


def section_list(list: []):
    field = []
    for item in list:
        field.append({
            "type": "mrkdwn",
            "text": item
        })
    return {
        "type": "section",
        "fields": [
            *field
        ]
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


def button(label: str, style: str, action_id: str = "", value: str = ""):
    return {
        "type": "button",
        "text": {
            "type": "plain_text",
            "emoji": True,
            "text": label
        },
        "value": value,
        "style": style,
        "action_id": action_id,
    }


def button_action(label: str, value: str = "submit", action_id: str = "", block_id: str = ""):
    return {
        "type": "actions",
        "block_id": block_id,
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": label,
                    "emoji": True,
                },
                "value": value,
                "action_id": action_id,
            }
        ]
    }


def divider():
    return {"type": "divider"}


def list_users_block_slack(title: str, placeholder: str, action_id: str = "", block_id: str = ""):
    return {
        "type": "section",
        "block_id": block_id,
        "text": {"type": "mrkdwn", "text": title},
        "accessory": {
            "type": "users_select",
            "placeholder": {
                "type": "plain_text",
                "text": placeholder,
                "emoji": True,
            },
            "action_id": action_id,
        },
    }


def input_text(label: str, action_id: str = "", block_id: str = "", multiline=False):
    return {
        "type": "input",
        "block_id": block_id,
        "element": {
            "type": "plain_text_input",
            "multiline": multiline,
            "action_id": action_id,
        },
        "label": {
            "type": "plain_text",
            "text": label,
            "emoji": True,
        },
    }


def input_select(options: dict, label: str = "", placeholder: str = "", action_id: str = "", block_id: str = ""):
    items = []
    for key, value in options.items():
        items.append({
            "text": {
                "type": "plain_text",
                "text": key,
                "emoji": True,
            },
            "value": value
        })

    return {
        "type": "input",
        "block_id": block_id,
        "element": {
            "type": "static_select",
            "placeholder":  {
                "type": "plain_text",
                "text": placeholder,
                "emoji": True,
            },
            "options": [
                *items
            ],
            "action_id": action_id
        },
        "label": {"type": "plain_text", "text": label, "emoji": True},
    }


def input_radio(options: dict, label: str = "", action_id: str = "", block_id: str = ""):
    items = []
    for key, value in options.items():
        items.append({
            "text": {
                "type": "plain_text",
                "text": key,
                "emoji": True,
            },
            "value": value
        })
    return {
        "type": "input",
        "block_id": block_id,
        "element": {
            "type": "radio_buttons",
            "options": [
                *items
            ],
            "action_id": action_id
        },
        "label": {"type": "plain_text", "text": label, "emoji": True},
    }


def input_select_users(label : str = "", action_id : str = ""):
    return {
        "type": "users_select",
        "placeholder": {
                "type": "plain_text",
                "text": label,
                "emoji": True,
        },
        "action_id": action_id,
    }
