class Menu:
    listOfMenuChoices = None
    selection = None

    def __init__(self,listOfChoicesChoosen):
        self.listOfMenuChoices = listOfChoicesChoosen
        self.showMenuChoices()
        self.askSelectionToUser()

    def showMenuChoices(self):
        for choice in self.listOfMenuChoices:
            print(choice)

    def askSelectionToUser(self):
        self.selection = input('What is your select ?')