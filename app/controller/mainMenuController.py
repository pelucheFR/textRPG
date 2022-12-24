from app.view.errorMessage import errorMessageView
from app.view.mainMenuView import mainMenu
from app.view.errorMessage import errorMessageView
from app.controller.newGameController import newGameController

def mainMenuController():
    selection = None

    selection = int(mainMenu())
    if(selection == 1):
        newGameController()
        return # Changer cela +tard
    if(selection > 1 and selection < 3):
        print('TEST: Controle OK')
    else:
        errorMessageView('Input Invalid')
        mainMenuController()