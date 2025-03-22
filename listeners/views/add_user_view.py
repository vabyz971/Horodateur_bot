from logging import Logger
import os
from slack_bolt import Ack
from slack_sdk import WebClient
from ..utils.verifications import is_user_admin
from models.User import UserModel
from sqlalchemy.orm import Session
from database import EngineDatabase

engine = EngineDatabase.start_engine()


def add_user_view_callback(ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()

        ## IS USER AN ADMIN
        if is_user_admin(body["user"]["id"]):
            view_submission = body["view"]["state"]["values"]
            logger.info(view_submission)
            id_user = view_submission["list_user_id"][
                "update_select_user_modal_action"
            ]["selected_user"]
            name_user = view_submission["name_user_id"]["name_user"]["value"]
            group_user = view_submission["group_user_id"]["group_user"][
                "selected_option"
            ]["value"]

            ## Add New user
            with Session(engine) as session:
                new_user = UserModel(
                    id_slack=id_user, name=name_user, groupe=group_user
                )
                session.add(new_user)
                session.commit()
                return client.chat_postMessage(
                    channel=body["user"]["id"],
                    text=f"L'utilisateur <@{name_user}> du groupe {group_user} a bien été ajouté",
                )

        else:
            return client.chat_postMessage(
                channel=body["user"]["id"], text="Vous n'êtes pas Admin !!!"
            )

    except Exception as e:
        logger.error(e)
        return client.chat_postMessage(
            channel=body["user"]["id"],
            text=f"Une erreur est survenue lors de l'ajout de l'utilisateur",
        )
