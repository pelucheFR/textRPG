import json
from app.model.Player import Player
from app.view.adventureView import adventureView

class adventureMenuController:
    def __init__(self):
        self.player = None
    
    def playAdventure(self):
        if(self.player == None):
            save = self.readSave()
            self.player = Player(save)
        choice = adventureView()

        if(choice == "dontwork"):
            self.playAdventure()

    def readSave(self):
        with open('data/save.json') as json_file:
            data = json.load(json_file)
        return data