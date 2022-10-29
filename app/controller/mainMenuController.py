from app.view.errorMessage import errorMessageView
from app.view.mainMenuView import mainMenu
from app.view.errorMessage import errorMessageView

def mainMenuController():
    selection = None

    selection = int(mainMenu())
    if(selection > 0 and selection < 3):
        print('TEST: Controle OK')
    else:
        errorMessageView('Input Invalid')
        mainMenuController()