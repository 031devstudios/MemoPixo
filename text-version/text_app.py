#############
## Imports ##
#############

import time,os,sys,random

###############
## Constants ##
###############



###############
## Variables ##
###############

player_name = ""
menu_selection = ""
difficulty = 1
sequence = []
player_answer = ""
player_sequence = []
game_running = True
colours = {"RED": 1, "BLUE": 2, "YELLOW": 3, "GREEN": 4}
player_converted_answer = []
player_score = 0

###############
## Functions ##
###############

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
  value = input('\n> ')  
  return value 

def clearScreen():
  os.system("cls")

def main_menu():
    typingPrint("\n\nN = New Game\nS = Settings\nH = Help\nQ = Quit")
    menu_selection = typingInput("")
    global difficulty
    if menu_selection == "n" or menu_selection == "N":
        pass
    elif menu_selection == "s" or menu_selection == "S":
        difficulty = int(typingInput("Set the difficulty. This affects the speed of the displayed sequence.\n1 = Easy\n2 = Medium\n3 = Hard"))
        if difficulty == 1:
            typingPrint(f"Difficulty set to {difficulty}.")
            time.sleep(1)
            main_menu()
        elif difficulty == 2:
            typingPrint(f"Difficulty set to {difficulty}.")
            time.sleep(1)
            main_menu()
        elif difficulty == 3:
            typingPrint(f"Difficulty set to {difficulty}.")
            time.sleep(1)
            main_menu()
    elif menu_selection == "h" or menu_selection == "H":
        typingPrint("The game will display a sequence of colours that the player will be required to remember.\nAt the end of the sequence the player will be required to type in the sequence in the correct order.\nIf the sequence is correct, a new sequence will be displayed and the player will score one point.\nIf an incorect sequence is entered, the game will end and display the players score.")
        main_menu()
    elif menu_selection == "q" or menu_selection == "Q":
        typingPrint("Thank you for playing. Goodbye.")
        time.sleep(1)
        clearScreen()
        sys.exit()
    else:
        typingPrint("Incorrect entry. Please try again.")
        main_menu()
            
    return difficulty

def generate_sequence():
    n = random.randint(1,4)
    sequence.append(n)

def display_colours(sequence, difficulty):
    if difficulty == 1:
        difficulty_time = 1
    elif difficulty == 2:
        difficulty_time = 0.65
    elif difficulty == 3:
        difficulty_time = 0.3

    for i in sequence:
        if i == 1:
            typingPrint("RED")
            time.sleep(difficulty_time)
            clearScreen()
        elif i == 2:
            typingPrint("BLUE")
            time.sleep(difficulty_time)
            clearScreen()
        elif i == 3:
            typingPrint("YELLOW")
            time.sleep(difficulty_time)
            clearScreen()
        elif i == 4:
            typingPrint("GREEN")
            time.sleep(difficulty_time)
            clearScreen()

def check_answer(sequence, player_score):
    check = True
    while check:
        player_answer = list(map(str, input("> ")))
        for i in player_answer:
            if i == 'r' or i == 'R' or i == 'RED' or i == 'red':
                player_converted_answer.append(1)
                check = False
            elif i == 'b' or i == 'B' or i == 'BLUE' or i == 'blue':
                player_converted_answer.append(2)
                check = False
            elif i == 'y' or i == 'Y' or i == 'YELLOW' or i == 'yellow':
                player_converted_answer.append(3)
                check = False
            elif i == 'g' or i == 'G' or i == 'GREEN' or i == 'green':
                player_converted_answer.append(4)
                check = False
            else:
                print("Incorrect entry. Type R - RED, B - BLUE, G - GREEN, Y - YELLOW.")
                player_converted_answer.clear()
    if player_converted_answer == sequence:
        typingPrint("CORRECT!")
        player_converted_answer.clear()
    else:
        typingPrint(f"You failed. Game Over! Your final score is {player_score}.")
        time.sleep(1)
        sys.exit()

def add_score(score):
    score += 1
    return score



def main():
    generate_sequence()
    display_colours(sequence, difficulty)
    check_answer(sequence, player_score)
    player_converted_answer.clear()
    time.sleep(1)
    clearScreen()
    
    
    
##########
## Main ##
##########

if __name__ == "__main__":
    clearScreen()
    typingPrint("Welcome to PixoMemo!\nThis is a text-based memory game.\nUse the corresponding letters to navigate the menus.")
    difficulty = main_menu()
    clearScreen()
    time.sleep(1)
    typingPrint(f"Difficulty set to level {difficulty}. Game starting in 3...")
    time.sleep(1)
    typingPrint("2...")
    time.sleep(1)
    typingPrint("1...")
    time.sleep(1)
    while game_running == True:
        clearScreen()
        main()
        player_score = add_score(player_score)
        typingPrint(f"Your score is: {player_score}\nGet ready for the next round...")
        time.sleep(1.5)
        clearScreen()