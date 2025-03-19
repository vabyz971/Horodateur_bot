from slack_bolt import App
from .sample_view import sample_view_callback
from .confirmation_google_view import confirmation_google_view_callback


def register(app: App):
    app.view("sample_view_id")(sample_view_callback)
    app.view("confirmation_google_view")(confirmation_google_view_callback)
