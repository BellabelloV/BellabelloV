import random
from datetime import datetime

""" 
High school students typically face boredom and
restlessness during the waiting period in class 
between classes. These brief durations, which often last 
between a few minutes and fifteen minutes, may contribute to boredom and disengagement. 
The goal is to create a simple and engaging Python-based
guessing game to address this common issue. 
The game has two purposes: first, it gives students an
intriguing activity to play on their devices, and 
second, it promotes engagement and cerebral 
stimulation during these brief waiting intervals. 
"""
#filename for game records
all_time_records_file_name = "attempts"
#total number of attempts for guessing
number_of_chances_for_game = 5

#instruction or guide for difficulty
difficulty_instructions = '''
Hello and welcome to the secret number guessing game.
Select your difficulty level to begin:
        1 - Easy (1-10)
        2 - Medium (11-40)
        3 - Hard (41-80)
        '''

#split text range into integers
#This function splits a given text with integers seperated by '-' into integers
#returns start: the beginning range value, end: Last range value
def split_text_to_integers(text):
    start,end = map(int, text.split('-'))
    return start, end

# The range selector function returns the range of values for
# guessing based on the level of difficulty selected by the player.
# The function takes the difficulty selected and returns the range in a string format.
def range_selector(selected_difficulty):
    if selected_difficulty == 1:
        return "1-10"
    elif selected_difficulty == 2:
        return "11-40"
    elif selected_difficulty == 3:
        return "41-80"
    else:
        return "0"

#This function checks if the difficulty selected 
# exists in the defined difficulty levels of the game. 
#The game has 3 levels of difficulty. Hence any level above three will be invalid.
#The function returns true if the level is valid and false otherwise.      
def verify_difficulty_selected(selected_difficulty):
    if 1 <= selected_difficulty <= 3:
        return True, ""
    return False, "Enter 1,2 or 3 to select a difficulty level"
    
#This Function contains a sequence of instruction to select the level of difficulty to be played.
#this function depends on the function to verify the difficulty level and the range selector function.
#Based on the level of difficulty selected, the range for guessing values is also defined.
#This function return two values: the level of difficulty selected, the range selected
def select_game_difficulty():
    print(difficulty_instructions)
    execute = True # Allow the function to run
    while execute: #while the function is allowed to execute
        selected_difficulty = int(input("\nEnter the difficulty level of choice: ")) # get difficulty level from use
        result, message = verify_difficulty_selected(selected_difficulty) 
        if result:
            execute = False
            return selected_difficulty, range_selector(selected_difficulty)
        else:
            print(message)
    
#This function generates and returns the secret number based on the level of
#difficulty selected.
def generate_secret_number_to_guess(selected_difficulty):
    if selected_difficulty == 1:
        return random.randint(1,10)
    elif selected_difficulty == 2:
        return random.randint(11,40)
    elif selected_difficulty == 3:
        return random.randint(41, 80)
    else:
        return 0
    
#The input paramenters for this function are:
# The number guessed by the player,
# The correct secret Value, 
# the range of numbers based on difficulty level.
# This function check the players guessed value against the actual value and returns
# a hint on how far the guess is from the actual value.
def result_check(player_guess,secret_number,difficulty_range=""):
    start, end = split_text_to_integers(difficulty_range)
    if not (start <= player_guess <= end): # if player's guess is not between the start and end range
        return f"Enter your guess between {start} and {end}", False
    elif player_guess == secret_number:
        return f"Congratulations! You guessed right. The answer is {player_guess}!", True
    elif player_guess < secret_number:
        return "Hint: The secret number is greater than your guess.", False
    else:
        return "Hint: The secret number is less than your guess.", False

#This function asks the player if they would like to play the game again
def ask_to_play_again():
    result = input("Would you like to play again? (yes/no)")
    if result == "yes":
        return True, ""
    return False, "Goodbye, Thanks for playing!!"

#This function contains the sequence of playing on guessing game bundle
# of 5 guesses.
def guess_game(selected_difficulty,difficulty_range):
    max_attempts = number_of_chances_for_game
    player_guesses = [] # all guessed numbers in the round
    end_game = False # should the game end or continue
    secret_number = generate_secret_number_to_guess(selected_difficulty) # store generated secret number.
    
    while max_attempts > 0 and not end_game: #while the number of attempts is greater than zero and game is allowed to run
        print(f"\n{max_attempts} chance(s) remaining")
        player_guess = int(input(f"Guess a number in the range {difficulty_range}: ")) # get input from user
        player_guesses.append(player_guess) # store guessed value
        result, end_game = result_check(player_guess, secret_number,difficulty_range) #get the result and decision to continue with the game.
        print(result)#print the result/hint to the player
        max_attempts -= 1 #minimize attempts of the player by 1
    if max_attempts == 0 and end_game == False: #print this only when the player has maxed out their guessing attempts
        print(f"Sorry you ran out of attempts. The correct number is {secret_number}\n")
    return player_guesses #return all the uesses made by the player

#Ask the player if they would like to view game history
def view_guesses():
    result = input("Would you like to view all the answers you guessed? (yes/no)")
    if result == "yes":
        read_data_from_file(all_time_records_file_name)
        return True
    return False

#This function writes data to a file with a given filename and title    
def write_data_to_file(attempts, filename, title):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(filename,"a") as file:
        file.write(f"\nAttempt N0: {title} @ {current_time}\n")
        for attempt in attempts:
            file.write(f"{attempt}\n")

# This function reads the records from a file named 'attempts'
# and prints results to the console.
def read_data_from_file(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.read()

        # Print the content to the console
        print("File Content:")
        print(file_content)

#This function executes the guessing game in a loop based on 
# the players decision to continue the game or not  
def game_play():
    continue_game = True # should the game run again or not
    number_of_times_user_played_game = 1 # number of times the player the guessing game at a sitting
    while continue_game:
        game_difficulty, difficulty_range = select_game_difficulty() # set ame difficulty and range of values
        player_guesses = guess_game(game_difficulty,difficulty_range) # get players guesses
        continue_game,message = ask_to_play_again() # set continue game status and message from decision to continue the game
        #Record game results
        write_data_to_file(player_guesses,all_time_records_file_name,number_of_times_user_played_game) #write results to file
        if continue_game: # if player decides to player again, increase number of play times by 1
            number_of_times_user_played_game += 1
    view_guesses()
    print(message)
    
if __name__=="__main__":    
    # start the game
    game_play()
