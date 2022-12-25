import json
from app.model.Player import Player
from app.controller.adventureController import adventureController

def loadGameController():
    with open("data/save.json", "r") as f:
        data = f.read()
    jsonification = json.loads(data)
    player = Player(**jsonification)
    print('Sauvegarde chargé\n')
    adventureController(player)
    jsonification = json.dumps(player.__dict__)
    with open("data/save.json", "w") as f:
        f.write(jsonification)