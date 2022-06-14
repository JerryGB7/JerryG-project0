import pickle 
import Event_system
from Class_management import Player
import os
import time

data_exists = os.path.isfile("test.pickle")

# Function to start the game or load any saved files
def start_load():
    # Check to see if there is already a saved data
    if data_exists:
        with open(f'test.pickle', 'rb') as f2:
            saved_player = pickle.load(f2)
            print(f"Welcome back {saved_player.name}!")
            time.sleep(1)
        return saved_player   
    # if there is no save data then start the intro
    else:
        os.system('cls')
        username = input("""
Welcome to My Zero Academy, where beginner hero's get their experience to become pros. 
You will be strengthening your body, mind, and abilities within 30 days. 
After 30 days you will be ready to move on to Pro hero status! 
But first please enter your name: """)
        os.system('cls')
        print("""
In this section you will be able to choose your own quirk to fight small enemies and gain experience.

1) The first quirk is the power of flight! However, you can only use this ability while you are holding your breath. The moment you breathe, you will plummet straight down.

2) The second quirk is the power of telekinesis! However, you can only telepathically carry things that you can carry with your real strength and it does not affect living things.

3) The third quirk is Flare up! This allows you to control the power of adrenaline and temporarily boost your power tremendously.""")
        
        # get the right type of input from user
        while True:
            try:
                quirk = int(input("\nNow which quirk would you like? Type 1, 2, or 3:  "))
                if quirk == 1 or quirk == 2 or quirk == 3:
                    break
                else:
                    print("Not a valid number")
            except ValueError:
                print("Please type 1, 2 or 3 only.")
                continue

        #Once the user puts in valid information, create a new save file with pickle.
        print("Now that you chose your powers, it's time to start your journey to becoming a pro hero! You can travel to places around the city.")
        new_player = Player(username, quirk)
        new_player.get_stats(new_player.id)
        with open(f'test.pickle', 'wb') as f:
            pickle.dump(new_player, f)
        return new_player      

# Function that displays player options and returns the number selected
def decision(): 
    d = input(f"""
    What would you like to do? Type the number next to the action you want to do.
    1) Find a random bad guy to fight. 
    2) Spend $40 to strength train at the gym. 
    3) Spend $20 to study at the library.
    4) Go to shop.
    5) Sleep to gain energy.
    i) View your character info.
    d) Delete Save Data.
    """)

    return d

# Using a loop to keep the game running until game is over
while True:
    os.system('cls')
    with open(f'test.pickle', 'rb') as f2:
        player = pickle.load(f2)
    print(f"""
    ---------------------------------------------------------------------------
    |Hero name: {player.hero_name}| 
    Current energy: {player.energy} / Current gold: ${player.gold} / Current day: {player.day}
    ---------------------------------------------------------------------------
    """)
    d = decision()
    if d == '1':
        Event_system.random_encounter()
    elif d == "2":
        Event_system.gym_option()
    elif d == "3":
        Event_system.library_option()
    elif d == "4":
        Event_system.shop_option()
    elif d == "5":
        Event_system.sleep_option()
    elif d == 'd':
        os.remove("test.pickle")
        print("Data has been deleted. Run the file again to start over!")
        time.sleep(3)
        break
    elif d == 'i':
        i = input(f"{player.hero_name}, {player.power}, {player.mana}. Press any key to close ... ")  
    else:
        print("Not an option. Please try again")
        time.sleep(1)
        continue    


