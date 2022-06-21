class Item:
    def __init__(self, name, price, effect):
        self.name = name
        self.price = price
        self.effect = effect
    
med = Item("Med Pack S", 30, "Heal")
smoke = Item("Smoke ball", 100, "Evade")
bat = Item("Metal bat", 120, "Stun")
