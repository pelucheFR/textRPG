from app.view.errorMessage import errorMessageView
from app.view.mainMenuView import mainMenu
from app.controller.newGameController import newGameController
from app.controller.loadGameController import loadGameController

def mainMenuController():
    choice = int(mainMenu())
    if(choice == 1):
        newGameController()
        return
    if(choice == 2):
        loadGameController()
        return
    if(choice == 3):
        return
    mainMenuController()
        