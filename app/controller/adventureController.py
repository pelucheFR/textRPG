from app.model.Player import Player
from app.view.adventureView import adventureView
from app.controller.combatController import combatController

def adventureController(player):
    playerChoice = adventureView()
    print(playerChoice)
    if(playerChoice == '1'):
        combatController()
    if(playerChoice == '2'):
        player.heal(player)
    if(playerChoice != '0'):
        adventureController(player)