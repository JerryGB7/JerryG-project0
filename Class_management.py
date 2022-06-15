class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.maxenergy = 2000
        self.power = 0
        self.mana = 0
        self.hero_name = ''
        self.gold = 100
        self.day = 1

    def get_stats(self, id):
        if id == 1:
            self.energy = 1000
            self.power = 100
            self.mana = 100
            self.hero_name = "Bird Breathless"
            self.moves = ["Flying kick", "Aerial tackle", "Egg drop", "Deep Breath"]
        elif id == 2:
            self.energy = 1200
            self.power = 80
            self.mana = 130
            self.hero_name = "Contact 0"
            self.moves = ["Rock barrage", "Precision shot", "Leg sweep", "E crash"]
        elif id == 3:
            self.energy = 700
            self.power = 180
            self.mana = 30 
            self.hero_name = "Nova Flare"
            self.moves = ["Drop kick", "Clothesline", "Suplex", "Flare up!"]


class Enemy:
    def __init__(self, name):
        self.name = name
        self.hp = 0 
        self.pw = 0
        self.gold = 0
        self.moves = []

    def get_small_enemy(self, name):
        if name == "RatMan":
            self.hp = 500
            self.pw = 50
            self.gold = 20
            self.moves = ["Scratch", "Tail whip", "Poison bite"]
        elif name == "SkinCrawler":
            self.hp = 300
            self.pw = 30
            self.gold = 10
            self.moves = ["Glare", "Skin Wrap", "Hollow wail"]
        elif name == "SnakeFingers":
            self.hp = 400
            self.pw = 40
            self.gold = 40
            self.moves = ["Snake Slap", "Venom spit", "Construct"]


