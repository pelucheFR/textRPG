from app.view.errorMessage import errorMessageView
from app.view.mainMenuView import mainMenu
from app.controller.characterCreationController import characterCreatorController

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
            self.index()
    
    def activePlayerChoice(self,choice):
        match choice:
            case 1:
                characterCreator = characterCreatorController()
                characterCreator.runCharacterCreation()
            case 2:
                print('TEST: Controle OK')

            case 3:
                print('TEST: Controle OK')