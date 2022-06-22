import save_and_load as SL
import Event_system as ES
import Class_management as CM
import os 
import time

data_exists = os.path.isfile("p_data.pickle")

def new_player_intro():
    os.system('cls')
    username = input("""
Welcome to My Zero Academy, where beginner hero's get their experience to become pros. 
You will be strengthening your body, mind, and abilities within 30 days. 
After 30 days you will be ready to move on to Pro hero status! 
But first please enter your name: """)
    os.system('cls')
    print("""
In this section you will be able to choose your own quirk to fight small enemies and gain experience.

1) The first power is the power of flight! However, you can only use this ability while you are holding your breath. The moment you breathe, you will plummet straight down.

2) The second power is the power of telekinesis! However, you can only telepathically carry things that you can carry with your real strength and it does not affect living things.

3) The third power is Flare up! This allows you to control the power of adrenaline and temporarily boost your power tremendously.""")
        
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
    return (username, quirk)

# Function to start the game or load any saved files
def start_or_load():
    # Check to see if there is already a saved data
    if data_exists:
        saved_player = SL.load_data()
        print(f"Welcome back {saved_player.name}!")
        time.sleep(1)
        #return saved_player   
    # if there is no save data then start the intro
    else:
        user_inputs = new_player_intro()
        new_player = CM.Player(user_inputs[0], user_inputs[1])
        new_player.get_stats(new_player.id)
        SL.save_data(new_player)           
   
start_or_load()
# Function that displays player options and returns the number selected
def decision(): 
    d = input(f"""    What would you like to do? Type the number next to the action you want to do.
    1) Find a random bad guy to fight. 
    2) Spend $40 to strength train at the gym. 
    3) Spend $20 to study at the library.
    4) Go to shop.
    5) Sleep to gain energy.
    ----------------------------------------------
    i) View your character info.
    d) Delete Save Data.
    e) Exit.
    """)
    return d

# Function to print header for text ui
def header(player):
    print(f"""
    ---------------------------------------------------------------------------
    |Hero name: {player.hero_name}| 
    Current energy: {player.energy} / Current gold: ${player.gold} / Current day: {player.day}
    ---------------------------------------------------------------------------""")

# Using a loop to keep the game running until game is over
def main():
    while True:
        os.system('cls')
        player = SL.load_data()
        if player.energy <=0:
           print("Your energy has depleted, you must rest for 3 whole days until you are good to fight again...")
           player.day += 3
           player.energy = 1000
           time.sleep(4)

        #print the text ui
        header(player)
        d = decision()

        if d == '1':
            ES.random_encounter(player)
        elif d == "2":
            ES.gym_option(player)
        elif d == "3":
            ES.bookshop_option(player)
        elif d == "4":
            ES.shop_option()
        elif d == "5":
            ES.sleep_option(player)
        elif d == 'd':
            os.remove("p_data.pickle")
            print("Data has been deleted. Run the file again to start over!")
            time.sleep(3)
            break
        elif d == 'i':
            i = input(f"Hero name: {player.hero_name}, Health: {player.health}, Power: {player.power}, Mana: {player.mana}. Press enter to close ... ")  
        elif d == 'e':
            break
        else:
            print("Not an option. Please try again")
            time.sleep(1)
            continue   

main()