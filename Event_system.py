import random
import time
import os
import Class_management
import save_and_load as sl
from Items_and_abilities.abilities import list_of_abilities

def random_encounter(player):
    chance = random.randint(1, 20)
    if chance in range(1,11):
        enemy_options = [Class_management.ratman, Class_management.skin, Class_management.snake]
        encounter = random.choice(enemy_options)
        print(f"You encountered a {encounter.name} while walking down the alley!\nPrepare for battle!")
    elif chance in range(11, 21):
        enemy_options = [Class_management.wolf, Class_management.spring, Class_management.scorch]
        encounter = random.choice(enemy_options)
        print(f"You encountered a {encounter.name} while walking down the alley!\nBe careful this one is strong!")
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
            player.power += random.choice(range(10, 20, 2))
            player.gold -= 40
            player.energy -= random.choice(range(100, 200))
            sl.save_data(player)
        else:
            return

def bookshop_option(player):
    os.system('cls')
    print(f"Current mana: {player.mana}, Gold: {player.gold}")
    if player.gold < 20:
        print("Sorry you do not have enough money to buy books.")
        time.sleep(2)
        return
    else:
        d = input(f"You have arrived at the bookstore, would you like to study? y/n ")
        if d == 'y':
            player.mana += 1
            print("You gained 1 mana.")
            player.gold -= 20
            player.energy -= random.choice(range(50, 100))
            rand = random.randint(1, 5)
            if len(list_of_abilities) > 0:
                randAbility = random.choice(list_of_abilities)
            else:
                i = input("No more abilities to learn for now.")
                return
            if rand in range(1,4):
                print("Congratulations you learned a new ability!")
                player.abilities.append(randAbility)
                list_of_abilities.remove(randAbility)
            i = input("Press ENTER to continue")    
            sl.save_data(player)
        else:
            return

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
        player.health += 500
        sl.save_data(player)
        return
    else:
        return 

def print_battle_UI(player, enemy, turn):
    print(f"""
                                                                                       HP: {enemy.hp}
                                                                                       {enemy.name}
                                                    vs                                 
        HP: {player.health}
        {player.hero_name}
                                                                                   
                                            Turn: {turn}
                                             -----------------------                                    
                                            | 1) Attack
                                            | 2) Ability  
                                            | 3) Utility  
                                            | 4) Run   
                                             ----------------------- 
        """)

def print_ability_list(player):
    if len(player.abilities) == 0:
        print("You have not learned any abilities.")
        i = input("Press to continue ...")
    for i, elem in enumerate(player.abilities):
        print(f"{i+1}) {elem.name}")

def start_battle(player, enemy):
    time.sleep(2)
    turn = 1
    battling = True
    while battling:
        print_battle_UI(player, enemy, turn)
        option = input()
        if option == '1':
            attack = random.randint(player.power - 5, player.power + 5)
            enemy_attack = random.randint(enemy.pw - 5, enemy.pw +5)
            if enemy.hp - attack <= 0:
                gain_gold = random.choice(range(enemy.gold -5, enemy.gold + 5))
                player.gold += gain_gold 
                player.energy -= 100
                print(f"{player.name} defeated {enemy.name} with {random.choice(player.moves)}")
                print(f"The battle is over, {player.name} has won!")
                print(f"{enemy.name} dropped {gain_gold} gold")
                sl.save_data(player)
                b = input(f"You used 100 energy to fight. Press enter to continue...")
                enemy.hp = enemy.maxhp
                break
            print(f"You used {random.choice(player.moves)}.\nYou dealt {attack}!")
            print(f"{enemy.name} attacked you with {random.choice(enemy.moves)}. \nThey dealt {enemy_attack}")
            enemy.hp -= attack
            player.health -= enemy_attack
            turn += 1
            time.sleep(2)
        elif option == '2':
            print_ability_list(player)
            turn += 1
            time.sleep(1)
        elif option == '3':
            turn += 1
            time.sleep(1)
        elif option == '4':
            print("You escaped from this battle.") 
            time.sleep(1)
            break
        else:
            print("Not an option.")
