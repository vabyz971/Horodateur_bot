import os



def is_user_admin(id_user: str) -> bool:
    """
    The function `is_user_admin` checks if a user is an admin based on their ID.
    
    :param id_user: The `id_user` parameter is a string representing the user ID of a user in a Slack
    workspace
    :type id_user: str
    :return: The function `is_user_admin` is returning a boolean value, either `True` or `False`, based
    on whether the `id_user` parameter is equal to the value retrieved from the environment variable
    `SLACK_ADMIN_USER`.
    """
    return id_user == os.getenv("SLACK_ADMIN_USER")