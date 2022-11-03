from app.view.characterCreatorView import characterCreatorMenu
from app.controller.adventureController import adventureMenuController
from app.model.Player import Player
import json


class characterCreatorController:
    def __init__(self):
        pass

    def runCharacterCreation(self):
        name = None
        jsonData = None

        name = characterCreatorMenu()

        newCharacterData = {
            'name': name,
            "level": 1,
            "gold": 0,
            "health": 10,
            "experience": 0
        }

        jsonData = json.dumps(Player(newCharacterData).__dict__)
        with open("data/save.json", "w") as outfile:
            outfile.write(jsonData)
