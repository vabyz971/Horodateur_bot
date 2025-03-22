from slack_bolt import App
from .sample_action import sample_action_callback
from .submit_horodateur_action import submit_horodateur_action_callback
from .add_user_action import add_user_action_callback
from .update_select_user_modal_action import update_select_user_modal_action_callback


def register(app: App):
    app.action("sample_action_id")(sample_action_callback)
    app.action("form.submit")(submit_horodateur_action_callback)
    app.action("add_user_action")(add_user_action_callback)
    app.action("update_select_user_modal_action")(update_select_user_modal_action_callback)
