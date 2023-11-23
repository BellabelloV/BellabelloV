import random
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

#instrunction or guid for difficulty
difficulty_instructions = '''
Select your difficulty level:
        1 - Easy (1-10)
        2 - Medium (11-40)
        3 - Hard (41-80)'''

#split text range into integers
def split_text_to_integers(text):
    start,end = map(int, text.split('-'))
    return start, end

# return range based on difficulty
def range_selector(selected_difficulty):
    if selected_difficulty == 1:
        return "1-10"
    elif selected_difficulty == 2:
        return "11-40"
    elif selected_difficulty == 3:
        return "41-80"
    else:
        return "0"
        
def verify_difficulty_selected(selected_difficulty):
    if 1 <= selected_difficulty <= 3:
        return True, ""
    return False, "Enter 1,2 or 3 to select a difficulty level"
    
#Select difficulty level for the game
def select_game_difficulty():
    print(difficulty_instructions)
    execute = True
    while execute:
        selected_difficulty = int(input("Enter the difficulty level of choice: "))
        result, message = verify_difficulty_selected(selected_difficulty)
        if result:
            execute = False
            return selected_difficulty, range_selector(selected_difficulty)
        else:
            print(message)
    
#Generate a random number based on difficulty level
def generate_secret_number_to_guess(selected_difficulty):
    if selected_difficulty == 1:
        return random.randint(1,10)
    elif selected_difficulty == 2:
        return random.randint(11,40)
    elif selected_difficulty == 3:
        return random.randint(41, 80)
    else:
        return 0
    
#check the number guessed by the player
def result_check(player_guess,secret_number,difficulty_range=""):
    start, end = split_text_to_integers(difficulty_range)
    if not (start <= player_guess <= end):
        return f"Please guess a number between {start} and {end}", False
    elif player_guess == secret_number:
        return f"Congratulations! You guessed right. The answer is {player_guess}!", True
    elif player_guess < secret_number:# if the guess is not as spected, hint is provided
        return "Too low. Go higher!.", False
    else:
        return "Too, high!  Go lower!", False

#Ask if player wnats to play again
def ask_to_play_again():
    result = input("Would you like to play again? (yes/no)")
    if result == "yes":
        return True, ""
    return False, "Goodbye, Thanks for playing!!"

#Guess game 
def guess_game(selected_difficulty,difficulty_range):
    max_attempts = 5
    count = 0
    end_game = False
    secret_number = generate_secret_number_to_guess(selected_difficulty)
    
    while count < max_attempts and not end_game:
        player_guess = int(input(f"Guess an number in the range {difficulty_range}: "))
        result, end_game = result_check(player_guess, secret_number,difficulty_range)
        print(result)
        count += 1
    
#Run Game play sequence   
def game_play():
    continue_game = True
    while continue_game:
        game_difficulty, difficulty_range = select_game_difficulty()
        guess_game(game_difficulty,difficulty_range)
        continue_game,message = ask_to_play_again()
    print(message)
    
if __name__=="__main__":    
    # start the game
    game_play()