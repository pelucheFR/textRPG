class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.level = dict['level']
        self.gold = dict['gold']
        self.health = dict['health']
        self.experience = dict['experience']