from logging import Logger
from slack_sdk import WebClient
from ..utils.elements_blocks import header, section, divider, input_radio, input_select, input_text, button_action, section_list


def selectedCompetencesOption():
    select_item = {}
    for i in range(22):
        if (i < 21):
            select_item[f'Compétence {i}'] = f"Compétence {i}"
        else:
            select_item[f'Compétence {i} (STAGE)'] = f"Compétence {i} (STAGE)"
    return select_item


def app_home_opened_callback(client: WebClient, event: dict, logger: Logger):
    # ignore the app_home_opened event for anything but the Home tab
    if event["tab"] != "home":
        return
    try:

        BLOCKS = [
            header("Indiquez votre présence à tous les cours (période de 3 heures)"),
            divider(),
            section(f"*Nom de l'élève :* <@{event['user']}>"),
            input_radio(
                label="Horodateur",
                action_id="form.horodateur",
                block_id="form_horodateur",
                options={
                    "Arrivée": "Arrivée",
                    "Départ hâtif": "Départ hâtif"
                }),
            input_radio(
                label="Période",
                action_id="form.periode",
                block_id="form_periode",
                options={
                    "AM :clock8:": "AM",
                    "PM :clock130:": "PM"}),
            input_radio(
                label="Présence",
                action_id="form.presence",
                block_id="form_presence",
                options={
                    "En classe": "En classe",
                    "À distance": "À distance"}),
            input_select(
                label="Compétence travaillée durant la période",
                placeholder="Sélectionner une compétence",
                action_id="form.competence",
                block_id="form_competence",
                options=selectedCompetencesOption()),
            header('As-tu quelque chose à ajouter ?'),
            section("Du genre, « ouin, j'avais oublié de puncher en arrivant mais je suis arrivé à 8h30 », ou bien « je vais devoir quitter entre 10h et 10h30 à cause d'un rendez-vous chez le blablabla... ». Tu vois le genre?"),
            input_text(
                label="Tu peux l'écrire ici dans la section Note.",
                multiline=True,
                action_id="form.note",
                block_id="form_note"),
            button_action(
                label="Valider",
                value="submit",
                block_id="form_submit",
                action_id="form.submit"),

        ]

        client.views_publish(
            user_id=event["user"],
            view={
                "type": "home",
                "blocks": BLOCKS,
            },
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
