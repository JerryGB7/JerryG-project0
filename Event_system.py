import random
import time
import os
from Class_management import Enemy
import save_and_load


def random_encounter(player):
    chance = random.randint(1, 10)
    print(chance)
    if chance in range(1,11):
        enemy_names = ["RatMan", "SkinCrawler", "SnakeFingers"]
        encounter = random.choice(enemy_names)
        print(f"You encountered a {encounter} while walking down the alley!\nPrepare for battle!")
    start_battle(player, encounter)   

def gym_option(player):
    os.system('cls')
    print(f"Current power: {player.power}, Gold: {player.gold}")
    if player.gold < 40:
        print("Sorry you do not have enough money to enter the gym.")
        time.sleep(2)
        return
    else:
        d = input(f"You have arrived at the gym, entry fee is $40 would you like to pay? y/n ")
        if d == 'y':
            player.power += 20
            player.gold -= 40
            player.energy -= random.choice(range(100, 200))
            save_and_load.save_data(player)
        else:
            return

def library_option(player):
    print("Closed of renovations, but when we open you will be able to learn abilities and increase your magic powers!")
    time.sleep(4)

def shop_option():
    print("Shop will be opening soon. We will be selling all kinds of utility!")
    time.sleep(4)

def sleep_option(player):
    d = input(f"""
    The number of days is {player.day}, would you like to move on to the next? y/n
    """)
    if d == 'y':
        player.day += 1
        if player.energy >= player.maxenergy - 100:
            player.energy == player.maxenergy
        elif player.energy < player.maxenergy - 500:
            player.energy += 500
        save_and_load.save_data(player)
        return
    else:
        return 

def print_battle_UI(player, enemy):
    print(f"""
                                                                                       HP: {enemy.hp}
                                                                                       {enemy.name}
                                                    vs                                 
        HP: {player.energy}
        {player.hero_name}
                                                                                   
                            
                                             -----------------------                                    
                                            | 1) Attack
                                            | 2) Ability  
                                            | 3) Utility  
                                            | 4) Run   
                                             ----------------------- 
        """)

def start_battle(player, enemy):
    n = Enemy(enemy)
    n.get_small_enemy(n.name)
    time.sleep(2)
    os.system('cls')
    battling = True
    while battling:
        print_battle_UI(player, n)
        option = input()
        if option == '1':
            attack = random.randint(player.power - 5, player.power + 5)
            enemy_attack = random.randint(n.pw - 5, n.pw +5)
            if n.hp - attack <= 0:
                gain_gold = random.choice(range(n.gold -5, n.gold + 5))
                player.gold += gain_gold 
                print(f"{player.name} defeated {n.name} with {random.choice(player.moves)}")
                print(f"The battle is over, {player.name} has won!")
                print(f"{n.name} dropped {gain_gold} gold")
                save_and_load.save_data(player)
                b = input("Press enter to continue...")
                break
            print(f"You used {random.choice(player.moves)}.\nYou dealt {attack}!")
            print(f"{n.name} attacked you with {random.choice(n.moves)}. \nThey dealt {enemy_attack}")
            n.hp -= attack
            player.energy -= enemy_attack
            time.sleep(1)
        elif option == '2':
            time.sleep(1)
        elif option == '3':
            time.sleep(1)
        elif option == '4':
            print("You escaped from this battle.") 
            time.sleep(1)
            break
