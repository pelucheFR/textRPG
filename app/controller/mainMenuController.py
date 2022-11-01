from app.view.errorMessage import errorMessageView
from app.view.mainMenuView import mainMenu
from app.controller.characterCreationController import characterCreatorController
from app.controller.adventureController import adventureMenuController

class mainMenuController:
    def __init__(self):
        pass

    def runMainMenu(self):
        selection = None

        selection = int(mainMenu())
        if(selection > 0 and selection < 4):
            self.activePlayerChoice(selection)
        else:
            errorMessageView('Input Invalid')
            self.runMainMenu()
    
    def activePlayerChoice(self,choice):
        match choice:
            case 1: # New Game
                characterCreatorController().runCharacterCreation()
                adventureMenuController().playAdventure()
            case 2: # Continue
                adventureMenuController().playAdventure()
            case 3: # Leave
                print("You leaving the game...")