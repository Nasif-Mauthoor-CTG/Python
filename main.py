from random import randint # We can call randint without writing random.randint()

# Rock paper scissors game
# User and computer pick rock paper scissors.
# Rock beats scissors, paper beats rock and scissors beat paper.

# Guideline:
# You are only allowed to print in main.
# Follow the instructions for every function.
# Put everything together in main.

# Start
# Print messages to user and run the other functions in order
def main():
    print('Welcome to the snake game.')
    winner = 'tie'

    while winner == 'tie':
        print('Pick rock/paper/scissors')
        user_input = pick_stance()

        comp_input = generate_stance()
        print('The CPU picked ', comp_input)

        winner = evaluate_winner(user_input, comp_input)
        print('You ', winner)


# Get input from user (Hint: input())
# Return 'rock', 'paper' or 'scissors'
def pick_stance():
    choice = input()
    return choice


# Get a randomly generated answer (Hint: randint(
# Return 'rock', 'paper' or 'scissors'
def generate_stance():
    array = ['rock', 'paper', 'scissors']
    number = randint(0, 2)
    return array[number]


# Return 'user', 'computer' or 'tie'
def evaluate_winner(user, cpu):
    if user == cpu:
        return 'tie'
    if user == 'rock':
        if cpu == 'paper':
            return 'lose'
        else :
            return 'win'
    if user == 'scissors':
        if cpu == 'rock':
            return 'lose'
        else :
            return 'win'
    if user == 'paper':
        if cpu == 'scissors':
            return 'lose'
        else :
            return 'win'


# Run this file if it's the main file
if __name__ == '__main__':
    main()
