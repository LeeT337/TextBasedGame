import time
import random;

from pydoc import synopsis
from os import system, name

########### Room selection variables ###########

key_greenhouse = False
key_canteen = False
key_lab = True  ####### Update when imported minigame
key_oxygen = True ####### Update when imported minigame
key_command = False
key_all = [key_greenhouse, key_canteen, key_lab, key_oxygen, key_command]

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

################################ OPENING OF GAME ##################################

##### INTRO FUNCTIONS #############
def player_name():
    name = input("What is your name?:\n")
    if name.isalpha() and len(name) < 10:
        print(f"{name.title()} Wakes up...")
    else:
        print("That doesn't sound right.Let\'s try that again...")
        return player_name()

def start_prompt():
  start = input("Do you want to save your crew? [Y/N]")
  if start == "y" or "Y":
      print("Game begins") #initiate game sequence
  elif start == "n" or "N":
    print("You heartless bastard!") #add a little blame-filled outro
    time.sleep(4)
    exit() #Exit game
  else:
    print("Wrong key. Please choose Y for 'yes' or N 'no'")
    return start_prompt()

def enter_pin():
  pin = input("ENTER YOUR 4 DIGIT PIN:\n")
  pin666 = ["666", "0666", "6660"]
  while True:
    if pin == pin666:
      print("""
Good Morning Prince of Darkness. I trust you had a great slumber. 
Your Pod is OPEN.
      """)
      break
    elif pin.isnumeric() and len(pin) == 4:
      print("""
PIN Correct.
Your Pod is OPEN.
      """)
      break
    else:
      print("""
PIN is made of 4 NUMBERS. 
Input your PIN.
      """)
      return enter_pin()


# # Game Begining sequence #
def game_begin():
    print("""
    ██    ██             ██████             ████████            ██                  █████  
    ██    ██            ██    ██               ██               ██                 ██   ██ 
    ██    ██            ██    ██               ██               ██                 ███████ 
    ██  ██             ██    ██               ██               ██                 ██   ██ 
    ████       ██      ██████      ██        ██        ██     ███████     ██     ██   ██ 
    
        *  *  V  O  Y  A  G  E     O  F     T  H  E     L  A  S  T     A  R  K  *  *
    """)
    time.sleep(2)

    print("Input game intro here")
    time.sleep(2)
    player_name()
    time.sleep(2)
    start_prompt()
    time.sleep(2)
    enter_pin()
    time.sleep(2)


########### RPSLS #################
# RPSLS Variables #
cpu_random = []
win = 0
loss = 0
draw = 0
win_count = []
loss_count = []
draw_count = []

def rps_minigame():
    global cpu_random, win, loss, draw
    print("\nChoose your action. Enter numbers from 1 to 5.")
    player_action = input(""" 
[1]: "Rock" | [2]: "Paper" | [3]: "Scissors" | [4]: "Lizard" | [5]: "Spock"\n""")
    while player_action.isnumeric() == False or int(player_action) > 6 or int(player_action) < 1:
      player_action = input("Wrong key - Try again!\n")

    # CPU Choice generator #    
    cpu_choice = ["rock", "paper", "scissors", "lizard", "spock"]
    cpu_random = random.choice(cpu_choice) 
    print("-------------------\n")
    print(f"HUGO has chosen {cpu_random.title()}")  

# Player Action #
    if int(player_action) == 1:
          print("You have chosen Rock!\n")
          if cpu_random == "rock":
            print("That's a draw!")
            draw += 1
          if cpu_random == "paper":
            print("Paper covers rock - You lose!")
            loss += 1
          if cpu_random == "scissors":
            print("Rock smashes scissors - You win!")
            win += 1
          if cpu_random == "lizard":
            print("Rock smashes lizard - You win!")
            win += 1
          if cpu_random == "spock":
            print("Spock vaporises rock - You lose!")
            loss += 1
    elif int(player_action) == 2:
        print("You have chosen Paper!\n")
        if cpu_random == "paper":
          print("That's a draw!")
          draw += 1
        if cpu_random == "rock":
          print("Paper covers rock - You win!")
          win += 1
        elif cpu_random == "spock":
          print("Paper disproves Spock - You win!")
          win += 1
        elif cpu_random == "lizard":
          print("Lizard eats paper - You Lose!")
          loss += 1
        elif cpu_random == "scissors":
          print("Scissors cut paper - You Lose!")
          loss += 1
    elif int(player_action) == 3:
        print("You have chosen Scissors!\n")
        if cpu_random == "scissors":
          print("That's a draw!")
          draw += 1
        if cpu_random == "paper":
          print("Scissors cut paper - You win!")
          win += 1
        elif cpu_random == "lizard":
          print("Scissors decapitates lizard - You win!")
          win += 1
        elif cpu_random == "rock":
          print("Rock crushes scissors - You Lose!") 
          loss += 1 
        elif cpu_random == "spock":
          print("Spock smashes scissors - You Lose!") 
          loss += 1     
    elif int(player_action) == 4:
        print("You have chosen Lizard!\n")
        if cpu_random == "lizard":
          print("That's a draw!")
          draw += 1
        if cpu_random == "paper":
          print("Lizard eats paper - You win!")
          win += 1
        elif cpu_random == "spock":
          print("Lizard poisons Spock - You win!")
          win += 1
        elif cpu_random == "rock":
          print("Rock crushes lizard - You Lose!") 
          loss += 1 
        elif cpu_random == "scissors":
          print("Scissors decapitates lizard - You Lose!")  
          loss += 1 
    elif int(player_action) == 5:
        print("You have chosen Spock! \U0001f596 \n")
        if cpu_random == "spock":
          print("That's a draw!")
          draw += 1
        if cpu_random == "scissors":
          print("Spock smashes scissors - You win!")
          win += 1
        elif cpu_random == "rock":
          print("Spock vaporizes rock - You win!")
          win += 1
        elif cpu_random == "paper":
          print("Paper disproves Spock - You Lose!")  
          loss += 1
        elif cpu_random == "lizard":
          print("Lizard poisons Spock - You Lose!") 
          loss += 1
    elif int(player_action) == 6:
        print("""You have chosen a "Joey Triabbiani Special"
F* FIRE! \U0001F525  Fire beats everything - You win""")
        win += 3
        room_select()

# Loop function #
def loop():
    for x in range(2):
      if rps_minigame():
          break
      else:
        rps_winner
    
# Function determining the winner #
def rps_winner():     
  global win, loss, draw, win_count, loss_count, draw_count
  print("-------------------")
  win_count = print("You have won %d times!" % win)
  loss_count = print("You have lost %d times!" % loss)
  draw_count = print("You have draw %d times!" % draw)
  print("-------------------\n")

  if win > draw and win > loss:
      print("HUGO: ... I let you win!")    
  elif loss > win and loss > draw:
      print("L-O-S-E-R!")
  elif draw > win and draw > loss:
      print("That's a Draw!")
  else:
      print("That's a Draw!")
  time.sleep(2)
  print("HUGO: OK. That got boring really fast, I'll let you go")  
  time.sleep(2)
  print("\n ## P O D   O P E N S ##  \n") 
  time.sleep(2)


def rpsls_introtext():
    print("""
    HUGO: It was a long time since I've had some fun. Let's play a little game before I can let you out.
    I trust you are familiar with my choice of entertainment, let's have a game of good 'ol Rock, Paper, Scissors, Lizard, Spock!
    I understand that you've been in deep sleep for a while and havn't had any coffee yet. Let me remind you the rules real quick:

    Scissors cuts paper.
    Paper covers rock.
    Rock crushes lizard.
    Lizard poisons Spock.
    Spock smashes scissors.
    Scissors decapitates lizard.
    Lizard eats paper.
    Paper disproves Spock.
    Spock vaporizes rock.
    Rock crushes scissors.

    SIMPLE. Let's Play!\U0001f596""")
    time.sleep(1)

############### RPSLS RUNNING SEQUENCE ##############
def start_rpsls():
    rpsls_introtext()
    rps_minigame()
    loop()
    rps_winner()      

############ GREENHOUSE SECTION #####################

#function starts as binary and turns into inputed text
def binary_text(string):
    length = len(string)
    binary = ""
    #creates binary digits
    for i in range(length):
        one_zero = random.randint(0, 1)
        binary += str(one_zero)
    print(binary, end="\r")

    output = ""
    #loop changes 1 binary digit to a letter at a time
    for i in range(length):
        time.sleep(0.02)

        #turns string to list
        binary = list(binary)

        #changes the binary digit to letter from string
        binary[i] = string[i]

        output = ""

        #turns list to string
        for k in range(length):
            output += binary[k]

        #prints output, deletes line after printed unless it is finished output
        if i == (length - 1):
            print(output)
        else:
            print(output, end="\r")


original_plants = [["alive", "Rose1", 6],
          ["dead", "Dandelion1", 2],
          ["dead", "Daffodil1", 8],
          ["dead", "Daffodil2", 7],
          ["alive", "Daffodil3", 11],
          ["alive", "Dandelion2", 4],
          ["alive", "Rose2", 10],
          ["dead", "Rose3", 13], 
          ["alive", "Dandelion3", 9], 
          ["dead", "Rose4", 1]]
plants = original_plants.copy()



def show_plants():
    global plants
    print(["Status", "Name", "Size"])
    print("----------------------------------------")
    for plant in plants:
        print(plant)



def are_there_dead_plants():
    global plants
    number_dead_plants = 0
    are_there_dead_plants = True
    for plant in plants:
        if plant[0] == "dead":
            number_dead_plants += 1
    if number_dead_plants > 0:
        return True
    else:
        return False



def check_if_input_valid(user_input): 
    potential_inputs = ["pop()", "pop(first)", "pop(last)",
                       "sort(size)", "sort(ascending, size)", "sort(decending, size)", "sort(name)", "sort(ascending, name)", "sort(descending, name)",
                       "random()", "reset"]
    return user_input in potential_inputs


def split_input(user_input):

    split = user_input.split("(")
    method = split[0]
    if "," in user_input:
        split = split[1].split(",")
        option = split[0]
        split = split[1].split(")")
        split = split[0].split(" ")
        atribute = split[1]
    else:
        split = split[1].split(")")
        atribute = split[0]
        option = None
    
    return [method, option, atribute]


def method_pop(option):
    global plants
    if option == "first":
        if plants[0][0] == "dead":
            plants.pop(0)
        else:
            print("Plant is not dead")
    else:
        if plants[len(plants) - 1][0] == "dead":
            plants.pop()
        else:
            print("Plant is not dead")


def method_sort(option, atribute):
    global plants
    new_plants_array = []
    if atribute == "size":
        
        sizes = []
        for plant in plants:
            sizes.append(plant[2])
        if option == "descending":
            sizes.sort(reverse = True)
        else:
            sizes.sort() 

        #use this list of 1 atribute to sort originl array            
        for size in sizes:
            for plant in plants:
                if size == plant[2]:
                    new_plants_array.append(plant)
        
        plants = new_plants_array



    elif atribute == "name":
        
        ordered_plant_names = []
        for plant in plants:
            ordered_plant_names.append(plant[1])
        if option == "descending":
            ordered_plant_names.sort(reverse = True)
        else:
            ordered_plant_names.sort()

        new_plants_array = []
        for plant_name in ordered_plant_names:
            for plant in plants:
                if plant_name == plant[1]:
                    new_plants_array.append(plant)


        plants = new_plants_array

times_randomised = 0

def method_randomise():
    global plants
    global times_randomised

    if times_randomised < 1:
        ordered_numbers = []
        for i in range(len(plants)):
            ordered_numbers.append(i)

        randomised_numbers = []
        for i in range(len(plants)):
            ran_num = random.randint(0, len(ordered_numbers) - 1)
            randomised_numbers.append(ordered_numbers.pop(ran_num))
        
        randomised_plants = []
        for i in range(len(plants)):
            randomised_plants.append(plants[randomised_numbers[i]])
        times_randomised += 1
        plants = randomised_plants


    else:
        print("You have already randomised, you can not do it again")

def method_reset():
    global plants
    global original_plants
    plants = original_plants.copy()


def manipulate(method, option, atribute):
    global plants
    if method == "pop":
        method_pop(atribute)

    
    if method == "sort":
        method_sort(option, atribute)

    if method == "random":
        method_randomise()
        
    if method == "reset":
        method_reset()


def dialog():
    binary_text("It has been awhile since the plants have been watered.")
    binary_text("Now many of the plants have died, I need you to remove the dead plants for me.")


def rules_binary():
    print("")
    binary_text("The rules are:")
    binary_text("You will be given an array of plants, you need to remove the dead ones")
    binary_text("The plant will be in the format: [alive/dead, name, size]")
    binary_text("You will have the following methods:")
    binary_text("pop()- By default it removes the last value, you can remove the first with pop(first)")
    binary_text("sort(atribute) - The atributes you can sort by are name and size ")
    binary_text("random() - Randomises plant positions, but can only be used once")
    binary_text("reset - Resets plant array to give you the original")
    print("")
    
def rules_normal():
    print("The rules are:")
    print("You will be given an array of plants, you need to remove the dead ones")
    print("The plant will be in the format: [alive/dead, name, size]")
    print("You will have the following methods:")
    print("pop()- By default it removes the last value, you can remove the first with pop(first)")
    print("sort(atribute) - The atributes you can sort by are name and size ")
    print("random() - Randomises plant positions, but can only be used once")
    print("reset - Resets plant array to give you the original")
    


def play_greenhouse():
    global key_greenhouse   
    global deadplants # checks if all deadplants are removed
    deadplants = True
    dialog()


   
    times_ran = 0
    while deadplants == True:
        if times_ran == 0:
            rules_binary()
            times_ran += 1
        else:
            rules_normal()
        #make sure user input is valid
        is_input_valid = False
        while is_input_valid != True:
            show_plants()
            user_input = input("Input your method, option and atribute: ")

            is_input_valid = check_if_input_valid(user_input)

            if is_input_valid == False:
                print("invalid input\n")
            
        print("Input is valid\n")


        
        if user_input == "random()":
            method = "random"
            option = None
            atribute = None
            
        elif user_input == "reset":
            method = "reset"
            option = None
            atribute = None

        #returns array in form [method, option, atribute]
        else:
            seperated = split_input(user_input)
            method = seperated[0]
            option = seperated[1]
            atribute = seperated[2]
        
        manipulate(method, option, atribute)

        deadplants = are_there_dead_plants()
        clear()

    show_plants()
    print("")
    binary_text("Thankyou, now all the dead plants have been removed")
    binary_text("Here is your key")
    time.sleep(1.5)
    key_greenhouse = True
    return room_select()


############## CANTEEN - OMO 9K ########################

########FUCTIONS & VARIABLES#############
hotdog = ["Bun", "Sausage", "Hotdog", "Onions", "Ketchup", "Mustard"]
bolognese = ["Pasta", "Cheese", "Mince", "Minced Meat", "Beef", "Tomato Sauce", "Tomato", "Tomatoes", "Onions"]
hamburger = ["Bun", "Roll", "Burger", "Patty", "Onions", "Lettuce", "Tomato", "Cheese", "Sauce", "Kechup"]
recipes = [hotdog, bolognese, hamburger]
attempts = 0
ingredient_list = None
chosen_recipe = None
#########################################



#player chooses recipe 
def choose_recipe():
    global ingredient_list
    chosen_recipe = input("What would you like to make? A Hotdog, Bolognese or Hamburger? \n").capitalize()
    if chosen_recipe.capitalize() == "Hotdog" or chosen_recipe == "Bolognese" or chosen_recipe == "Hamburger":
        print(f"You chose to make a {chosen_recipe.capitalize()}. Excellent choice flesh face...I mean sir! \n")
        ingredient_list = chosen_recipe.capitalize()
        return chosen_recipe.capitalize()
    else:
        print("Please choose a valid recipe")
        return choose_recipe



#player lists ingredient and program checks if true in recipe
def check_ingredients_hotdog(chosen_recipe):
    for ingredients in hotdog or ingredients in bolognese or ingredients in hamburger:
        list_ingredients = input(f"Now type 1 ingredient needed to make your chosen meal & you should be good to go: \n").capitalize()
        time.sleep(2)
        if list_ingredients in hotdog or list_ingredients in bolognese or list_ingredients in hamburger:
            print(f"Great job, you just used the MIX-O-MATIC and made a meal! That wasn't so hard was it... \n")
            return check_ingredients_hotdog
        else:
            print("Not quite, try another one?")

#Introduction & Synopsis of objective
def introduction(synopsis):
    print("Hi there, “HUGO” here! \n")
    time.sleep(2)
    print("It seems you've found your way into the “Canteen”. Here you have access to the MIX-O-MATIC food printer which allows crew members to make a meal of their choice based on the ingredients available in the database. \n")
    time.sleep(4)
    print("You're a human, you like to eat right? \n")
    player = input("Yes or No?: \n").capitalize()
    if player.capitalize() == "Yes":
        print("Ahh that meat suit needing some fuel huh... \n")
    else:
        print("That's odd, I don't sense any bio circuitry in you... \n")
    print("Anyway... Why don't you have a go at making something in the MIX-O-MATIC. \n")
    time.sleep(4)

#############################################################
#Outro & Key
def mission_objective():
    global key_canteen
    print("CONGRATULATIONS HUMAN, YOU WIN! Here's your meal and a prize for playing the game.")
    key_canteen = True
    time.sleep(3)
    return room_select()
#############################################################

def play_canteen():
    introduction(synopsis)
    choose_recipe()
    check_ingredients_hotdog(chosen_recipe)
    mission_objective()



################# Comand Deck Py ##################

########## Declare Variables for Command Deck ###############

consoles = ['1', '2', '3']
current_console = None

########## Declare Functions ###############

def gap():
    print('\n')

def scene_intro():
    print('You head towards the Command Deck\n')
    input("Press enter to coninue\n")
    print('As you slowly walk through aluminium passageways you notice words of wisdom marked into the ceiling')
    time.sleep(4)
    print('"If I have seen further than most, it is because I have stood upon the shoulders of giants." I. Newton.\n')
    time.sleep(4)
    print('After navigating through these halls, you arrive on the main deck.')
    time.sleep(3)
    print('You see three black command consoles at the front of the room.\n')
    time.sleep(3)


def choose_console():
    global consoles #### gets the global variable for this section - 'consoles'
    
    ########## check that there are still consoles / riddles to be solved
    if len(consoles) > 0:
        global current_console

        console_choice = input(f'Which console do you choose to approach? {consoles}\n')
        
        for console in consoles:
            if console == console_choice:
                clear()
                print(f'You move over to console {console}')
                current_console = console
                launch_riddle()
                return choose_console()
            ##### EDGE CASE - User inputs values 1, 2 or 3 despite being completed ####
            elif console_choice != '1' or console_choice != "2" or console_choice != "3":
                print('You must choose one of the console terminals.')
                return choose_console()
    else:
        current_console = "puzzle completed"
        launch_riddle()



def launch_riddle():
    if current_console == "1":
        console_1_riddle()
    elif current_console == "2":
        console_2_riddle()
    elif current_console == "3":
        console_3_riddle()
    elif current_console == "puzzle completed":
        give_player_key()


def console_1_riddle():
    global consoles
    if consoles[0] != "1":
        print("Select a different console.")
        gap()
        time.sleep(2)
        return choose_console()
    
    answer = "Love"
    print('The console reads:\n\n')
    gap()
    binary_text('Before you reawaken humanity, you must prove that you understand what it is to be human')
    binary_text('Show that you know what being human means by answering the following riddle:')
    gap()
    #### Clue Round 1 ####
    #### Use the binary text function for all text given by the machine
    #### Keep inputs as blank and call binary text on the line before for the prompt
    binary_text("I can make people happy, I can make people cry.")
    binary_text("I can make people want me, and I can drive people crazy.")
    gap()
    binary_text("What am I?")
    player_answer = input()
    gap()

    #### Check if correct ####
    if player_answer.capitalize() == answer:
        consoles.remove("1")
        binary_text("Love must always be an answer, if humanity is to rebuild to it's former glory.")
        gap()
        time.sleep(2)
        return choose_console()
    else:
        clear()
        print(f'{player_answer.capitalize()} is not the right answer.')
        binary_text('Here is another clue to help you:')
        gap()
        
        ##### Clue Round 2 ####
        binary_text("I am invisible")
        binary_text("I make people suffer from symptoms like sweating and nausea")
        binary_text("and yet people can't survive without me.")
        gap()
        binary_text("What am I?")
        player_answer = input()
        
        #### Check if correct ####
        if player_answer.capitalize() == answer:
            gap()
            consoles.remove("1")
            binary_text("Love must always be an answer, if humanity is to rebuild to it's former glory.")
            time.sleep(2)
            return choose_console()
        else:
            clear()
            print(f'{player_answer.capitalize()} is not the right answer.')
            binary_text('Here is another clue to help you:')
            gap()
            
            #### Clue Round 3 ####
            binary_text("I can be blind, I can be powerful.")
            binary_text("I can be difficult, deep, complicated, and tender at the same time.")
            gap()
            binary_text("What am I?")
            player_answer = input()
            gap()
            
            #### Check if correct ####
            if player_answer.capitalize() == answer:
                consoles.remove("1")
                binary_text("Love must always be an answer, if humanity is to rebuild to it\'s former glory.")
                gap()
                time.sleep(2)
                return choose_console()
            
            else:
                gap()
                print(f'{player_answer.capitalize()} is not the right answer.')
                binary_text('You have not found the answer, come back to console 1 to try again')
                time.sleep(2)
                return choose_console()


def console_2_riddle():
    global consoles
    answer = "Imagination"

    binary_text("Before you reawaken humanity, you must prove that you understand what it is to be human")
    binary_text('Show that you know what being human means by answering the following riddle:')
    gap()
    
    #### Clue Round 1 ####
    binary_text("I am the future that may never happen.")
    binary_text("I am the only weapon in the war against reality.")
    gap()
    binary_text("What am I?")
    player_answer = input()
    gap()

    #### Check if correct ####
    if player_answer.capitalize() == answer:
        consoles.remove("2")
        binary_text('Imagination is fundamental to our experience of life, and will serve us well in the future.')
        time.sleep(2)
        return choose_console()

    else:
        clear()
        print(f'{player_answer} is not the right answer.')
        binary_text('Here is another clue to help you:')
        gap()
        
        ##### Clue Round 2 ####
        binary_text("A book shall ignite me.")
        binary_text("A mystery shall delight me.")
        binary_text("The artist shall invite me.")
        gap()
        binary_text("What am I?")
        player_answer = input()
        gap()
        
        #### Check if correct ####
        if player_answer.capitalize() == answer:
            consoles.remove("2")
            binary_text('Imagination is fundamental to our experience of life, and will serve us well in the future.')
            time.sleep(2)
            return choose_console()
        else:
            clear()
            print(f'{player_answer.capitalize()} is not the right answer.')
            binary_text('Here is another clue to help you:')
            gap()

            #### Clue Round 3 ####
            binary_text("I can carry you to worlds that have never existed.")
            binary_text("And yet, without me, you would go nowhere.")
            gap()
            binary_text("What am I?")
            player_answer = input()
            gap()

            #### Check if correct ####
            if player_answer.capitalize() == answer:
                consoles.remove("2")
                binary_text('Imagination is fundamental to our experience of life, and will serve us well in the future.')
                return choose_console()
            else:
                print(f'{player_answer.capitalize()} is not the right answer.')
                gap()
                binary_text('You have not found the answer, come back to console 2 to try again')
                time.sleep(2)
                return choose_console()


def console_3_riddle():
    global consoles
    answer = "Responsibility"

    binary_text('Before you reawaken humanity, you must prove that you understand what it is to be human')
    binary_text('Show that you know what being human means by answering the following riddle:')
    gap()
    
    #### Clue Round 1 ####
    binary_text("I am the price of greatness and the banishment of regret.")
    binary_text("I am the greatest source of meaning of which a man must not forget.")
    gap()
    binary_text("What am I?")
    player_answer = input()
    gap()
    
    #### Check if correct ####
    if player_answer.capitalize() == answer:
        consoles.remove("3")
        binary_text('Responsibility is essential to the the work you do. Without it we are all lost.')
        time.sleep(2)
        return choose_console()
    else:
        clear()
        print(f'{player_answer.capitalize()} is not the right answer.')
        binary_text('Here is another clue to help you:\n\n')
        gap()

        ##### Clue Round 2 ####
        binary_text("You cannot change the circumstances, the seasons, or the wind,")
        binary_text("but you can change yourself by embracing me.")
        gap()
        binary_text("What am I?")
        player_answer = input()
        gap()

        #### Check if correct ####
        if player_answer.capitalize() == answer:
            consoles.remove("3")
            binary_text('Responsibility is essential to the the work you do. Without it we are all lost.')
            time.sleep(2)
            return choose_console()
        else:
            clear()
            print(f'{player_answer.capitalize()} is not the right answer.')
            binary_text('Here is another clue to help you:')
            gap()

            #### Clue Round 3 ####
            binary_text("I come with freedom.")
            binary_text("I come with priviledge.")
            binary_text("I come with great power")
            gap()
            binary_text("What am I?")
            player_answer = input()
            gap()

            #### Check if correct ####
            if player_answer.capitalize() == answer:
                consoles.remove("3")
                binary_text('Responsibility is essential to the the work you do. Without it we are all lost.')
                time.sleep(2)
                return choose_console()
            else:
                gap()
                print(f'{player_answer.capitalize()} is not the right answer.')
                binary_text('You have not found the answer, come back to console 3 to try again')
                time.sleep(2)
                return choose_console()



def give_player_key():
    global key_command
    print(f'{name} receives key')
    print("You can now move onto the next section of the game.")
    key_command = True
    return room_select()

######### Command Deck Function ###########

def play_command():
    clear()
    scene_intro()
    choose_console()



##################### ROOM SELECTION #######################

# Room Selection #
def room_select():
 global key_greenhouse, key_canteen, key_command, key_oxygen, key_lab, key_all

 print("You must collect all five keys to awaken the Ark crew members")
 print("""
1 - Greenhouse
2 - Canteen
3 - Oxygen generator
4 - Laboratory
5 - Command Deck""")

 if key_greenhouse == True and key_canteen == True and key_command == True and key_lab == True and key_oxygen == True:
    game_win()

 room_choice = input("Which room do you want to go to: [1] [2] [3 - NOT FINISHED] [4 - NOT FINISHED] [5] \n")
 if room_choice == "1" and key_greenhouse == 0:
    return play_greenhouse()
 elif room_choice == "2" and key_canteen == 0:
    return play_canteen()
 elif room_choice == "3"and key_oxygen == 0:
    print("Sorry, We haven't finished that game yet.")
    time.sleep(5)
    return room_choice()
 elif room_choice == "4" and key_lab == 0:
    print("Sorry, We haven't finished that game yet.")
    time.sleep(5)
    return room_choice()
 elif room_choice == "5"and key_command == 0:
    return play_command()
 elif room_choice == "1" and key_greenhouse == 1:
    print("You've already completed this room")  
    return room_select() 
 elif room_choice == "2" and key_canteen == 1:
    print("You've already completed this room")  
    return room_select() 
 elif room_choice == "3" and key_oxygen == 1:
    print("You've already completed this room")  
    return room_select() 
 elif room_choice == "4" and key_lab == 1:
    print("You've already completed this room")  
    return room_select() 
 elif room_choice == "5" and key_command == 1:
    print("You've already completed this room")  
    return room_select() 
 else:
    print("Please choose a valid option")
    return room_select()


def game_win():
    clear()
    print("""You've entered all required keys to the console""")
    print("You win, you are the best!")
    time.sleep(10)
    exit()


############## RUN ROOM SELECT ###################

game_begin()
time.sleep(3)
clear()
start_rpsls()
room_select()