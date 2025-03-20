from slack_bolt import Ack, Respond
from logging import Logger
from sqlalchemy.orm import Session
from database import EngineDatabase
from models.User import UserModel


engine = EngineDatabase.start_engine()

def add_user_callback(command, ack: Ack, respond: Respond, logger: Logger):
    try:
        ack()
        with Session(engine) as session:
            arguments : list[str] = command["text"].split("|")
            logger.info(arguments)
            if arguments:
                user = UserModel(id_slack=arguments[0],name=arguments[1], groupe=arguments[2])
                session.add(user)
                session.commit()
                print("User saved successfully ！")
                respond("User saved successfully ！")
            
        if(user):
            print("User saved successfully!")
            respond("User saved successfully !")
            
        else:
            print("Error while saving the user.")
            respond("Error while saving the user.")
        
    except Exception as e:
        logger.error(e)
