def adventureView():
    listOfMenuChoices = [
        '1 - Combat',
        '2 - Tavern'
    ]

    for choice in listOfMenuChoices:
            print(choice)
    return input('What do you want to do ?\n')