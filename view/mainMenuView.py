def mainMenu():
    listOfMenuChoices = [
        '1 - New Game',
        '2 - Load Game',
        '3 - Leave Game'
    ]

    for choice in listOfMenuChoices:
            print(choice)

    return input('What is your select ?')


