import random
from random import randint
import time
import pickle
import os
from Class_management import Enemy

data_exists = os.path.isfile("test.pickle")
if data_exists:
    with open(f'test.pickle', 'rb') as f2:
        player = pickle.load(f2)

def random_encounter():
    chance = randint(1, 11)
    if chance in range(1,11):
        enemy_names = ["RatMan", "SkinCrawler", "SnakeFingers"]
        encounter = random.choice(enemy_names)
        print(f"You encountered a {encounter} while walking down the alley!\nPrepare for battle!")
    start_battle(player, encounter)   

def gym_option():
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
            with open(f'test.pickle', 'wb') as f:
                    pickle.dump(player, f)
        else:
            return

def library_option():
    pass

def shop_option():
    pass

def sleep_option():
    d = input(f"""
    The number of days is {player.day}, would you like to move on to the next? y/n
    """)
    if d == 'y':
        player.day += 1
        if player.energy >= player.maxenergy - 499:
            player.energy == player.maxenergy
        elif player.energy < player.maxenery - 500:
            player.energy += 500
        with open(f'test.pickle', 'wb') as f:
                pickle.dump(player, f)
        return
    else:
        return 

def start_battle(player, enemy):
    n = Enemy(enemy)
    n.get_small_enemy(n.name)
    time.sleep(2)
    os.system('cls')
    battling = True
    while battling:
        print(f"""
                                                                                       HP: {n.hp}
                                                                                       {n.name}
                                                    vs                                 
        HP: {player.energy}
        {player.hero_name}
                                                                                   

                                            
                                             -----------------------                                    
                                            | 1) Attack
                                            | 2) Block  
                                            | 3) Item  
                                            | 4) Run   
                                             ----------------------- 
        """)
        option = input()
        if option == '1':
            attack = randint(player.power - 5, player.power + 5)
            enemy_attack = randint(n.pw - 5, n.pw +5)
            if n.hp - attack <= 0:
                gain_gold = random.choice(range(n.gold -5, n.gold + 5))
                player.gold += gain_gold 
                print(f"{player.name} finished off {n.name} with {random.choice(player.moves)}")
                print(f"The battle is over, {player.name} has won!")
                print(f"{n.name} dropped {gain_gold} gold")
                with open(f'test.pickle', 'wb') as f:
                    pickle.dump(player, f)
                time.sleep(2)
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
