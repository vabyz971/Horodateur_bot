from slack_bolt import App
from .sample_command import sample_command_callback
from .infos_command import infos_command_callback
from .list_user_command import list_user_callback
from .add_user_command import add_user_callback


def register(app: App):
    app.command("/test")(sample_command_callback)
    app.command("/infos")(infos_command_callback)
    app.command("/list_users")(list_user_callback)
    app.command("/add_user")(add_user_callback)
