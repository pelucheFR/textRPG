from app.view.characterCreatorView import characterCreatorMenu
from app.model.Player import Player
import json

class characterCreatorController:
    def __init__(self):
        pass

    def runCharacterCreation(self):
        name = None
        jsonStr = None

        name = characterCreatorMenu()
        jsonStr = json.dumps(Player(name).__dict__)
        with open("data/save.json", "w") as outfile:
            outfile.write(jsonStr)
        