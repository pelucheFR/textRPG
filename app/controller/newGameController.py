from app.view.errorMessage import errorMessageView
from app.view.characterCreatorView import characterCreator
from app.model.Player import Player
import json

def newGameController():
    dataFromView = characterCreator()
    player = Player(dataFromView, 1, 2, 2, 2)
    jsonification = json.dumps(player.__dict__)
    with open("data/save.json", "w") as f:
        f.write(jsonification)