from model import Menu

listOfMenuChoices = [
    '1 - New Game',
    '2 - Load Game',
    '3 - Leave Game'
]

selection = Menu.Menu(listOfMenuChoices).selection

match int(selection):
            case 1:
                print('Start a new game')
            case 2:
                print('Load your game')
            case 3:
                print('Leave the game')
            case _:
                print('Not a valid selection')
