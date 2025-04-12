from slack_bolt import App
from .submit_horodateur_action import submit_horodateur_action_callback
from .update_select_user_modal_action import update_select_user_modal_action_callback


def register(app: App):
    app.action("form.submit")(submit_horodateur_action_callback)
    app.action("update_select_user_modal_action")(update_select_user_modal_action_callback)
