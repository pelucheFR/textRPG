class Player:
    def __init__(self, name, level, force, agility, intelligence):
        self.name = name
        self.level = level
        self.force = force
        self.agility = agility
        self.intelligence = intelligence
        self.health = 10
        
    def attack(self, cible):
        degats = self.force // 2
        cible.vie -= degats
        print(f"{self.name} attaque {cible.name} et lui inflige {degats} points de dégâts")
        
    def heal(self, cible):
        heals = self.intelligence * 2
        cible.vie += heals
        print(f"{self.name} soigne {cible.name} et lui redonne {heals} points de vie")