from slack_bolt import App
from .sample_command import sample_command_callback
from .infos_command import infos_command_callback


def register(app: App):
    app.command("/sample-command")(sample_command_callback)
    app.command("/infos")(infos_command_callback)
