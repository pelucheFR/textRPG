from view import mainMenuView

def mainMenuController():
    selection = int(mainMenuView.mainMenu())
    
    if(selection > 0 & selection < 3):
        print('TEST: Controle OK')
    else:
        print('TEST: C\'est d\'la marde')