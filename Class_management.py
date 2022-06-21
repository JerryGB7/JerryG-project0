class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.health = 0
        self.maxenergy = 2000
        self.power = 0
        self.mana = 0
        self.hero_name = ''
        self.gold = 100
        self.day = 1
        self.abilities = []

    def get_stats(self, id):
        if id == 1:
            self.energy = 1000
            self.health = 1000
            self.power = 100
            self.mana = 5
            self.hero_name = "Bird Breathless"
            self.moves = ["Flying kick", "Aerial tackle", "Egg drop"]
        elif id == 2:
            self.energy = 1000
            self.health = 1500
            self.power = 50
            self.mana = 13
            self.hero_name = "Contact 0"
            self.moves = ["Rock barrage", "Precision shot", "Leg sweep"]
        elif id == 3:
            self.energy = 1000
            self.health = 700
            self.power = 180
            self.mana = 2 
            self.hero_name = "Nova Flare"
            self.moves = ["Drop kick", "Clothesline", "Suplex"]


class Enemy:
    def __init__(self, name, maxhp, hp, pw, gold, moves):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp 
        self.pw = pw
        self.gold = gold
        self.moves = moves

ratman = Enemy("Ratman", 500, 500, 50, 30, moves=["Rat rush", "Bite", "Tail whip"])
snake = Enemy("SnakeFingers", 400, 400, 40, 50, moves=["Rat rush", "Bite", "Tail whip"])
skin = Enemy("SkinCrawler", 300, 300, 30, 10, moves=["Rat rush", "Bite", "Tail whip"])
wolf = Enemy("WolfWalker", 1200, 1200, 100, 120, moves=["Rat rush", "Bite", "Tail whip"])
spring = Enemy("SpringKicker", 1500, 1500, 130, 100, moves=["Rat rush", "Bite", "Tail whip"])
scorch = Enemy("Scorcher", 2000, 2000, 200, 250, moves=["Blaze", "Roast", "Flamethrower"])


