class Ability:
    def __init__(self, name, effect, cost):
        self.name = name
        self.effect = effect
        self.cost = cost
    

fly = Ability("fly", "stall", 2)
grasp = Ability("grasp", "stun", 2)
flare_up = Ability("Flare up", "double", 2)
list_of_abilities = [fly, grasp, flare_up]