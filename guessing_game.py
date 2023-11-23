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

# this is to get player's guess
def get_player_guess(all_attempts, filename):
    with open(filename,"a") as file :
        for attempt in all_attempts:
            file.write(f"{attempt}\n")
    # Get the player's guess and convert it to an integer
    guess = int(input("Enter your guess: "))
    return guess # number that was inputed or guesed by the user

#   feedback on the result, after a guessed attempt 
def result(player_guess, secret_number):
    # Check if the player's guess matches the secret number
    if player_guess == secret_number:
        return f'Congratulations! You won in the first attempt!'
    elif player_guess < secret_number:# if the guess is not as spected, hint is provided
        return "Too low. Try another attempt!."
    else:
        return "Too, high!  Try another attempt!"

# players to select the level of difficulty
def select_level_of_difficulty():
    # Display options for the player to choose the level of difficulty
    print("Choose the level of difficulty:")
    print("1. Easy (1-10)")# each level has a range of number that is expected to be inputed by player
    print("2. Medium (11-40)")
    print("3. Hard (41-80)")
    #  players get to select the level at which they want to start at
    level = int(input("Enter the level of choice "))
    return level

# this determine difficulty parameters for player
def get_secret_num(level):
    # Set difficulty parameters based on the selected level
    if level==1:
        return random.randint(1, 10)
    elif level==2:
        return random.randint(11, 40) 
    elif level==3:
        return random.randint(41, 80) 
    else:
        return None# end the game if the wrong level is inputed
#  this function initiates the play of the guessing game

def begin_guess():
    max_attempt = 5  # game is expected to stop after 5  maximum attempts

    while True:# players get to pick the level of difficulty
        level = select_level_of_difficulty()
        secret_number= get_secret_num(level)
        #print(secret_number)
        #secret_number = random.choice(SECRET_NUMBERS[:start_range])# generate winning number 
        if secret_number == None :
            print("invalid")# if the wrong number is inputed end the game
            break# after an invalid input end the game will end 
        print(f'selected winning secret number for level {level}')
        
        all_attempts=[]# keep all guessed attempts that were entered
         
        attempt=0 #initializing score
        while attempt < max_attempt: 
            player_guess_num= get_player_guess(all_attempts, "filename.text")# after the player guess the number 
            attempt += 1 # increase the number of guess by 1
            all_attempts.append(player_guess_num)# add all attempts that were made to this list 

            # Check if the player's guess is correct, if the guess is the same as the secret number
            if player_guess_num == secret_number:
                print(f"Congrats! You guessed correctly in {attempt} attempts!")# tells players they won afer this number of attempts
                break
            elif player_guess_num > secret_number:#give player ideas about what to expect number 
                print("Hint: The secret number is less than your guess.")
            else:
                print("Hint: The secret number is greater than your guess.")
            
        # Inform the player if they have run out of attempts
        if attempt == max_attempt:
            print(f"Sorry, you ran out of attempts. The correct number was {secret_number}.")
            get_player_guess(all_attempts,"attempts.txt")
        
        for  i in range(len(all_attempts)):
              print(all_attempts[i])

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":# if player wish to end the game
            print("Thanks for playing! Goodbye.")
            break

if __name__=="__main__":    
    # start the game
    begin_guess()
