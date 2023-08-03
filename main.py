import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    
    if guess > answer:
        print("Too high.")
        return turns -1
    elif guess < answer:
        print("Too low.")
        return turns -1
    else: 
        print(f"Your guess is: {guess}. You guessed the correct number!")
    
#Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #Ask user to guess a number beetween 1-100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Hint: the correct answer is {answer}.")
    
    turns = set_difficulty()
    
    
    #Repeating the guessing functionality if the get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Ask user to guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()
