# Building a Guessing Game

print("Hello friend! Welcome to the game of guesses!")
player_name = input("What is your name?")
wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
# Creating a secret word
secret_word = "python"
# Creating a Guess variable using the input statement to prompt the user to make a guess
guess = input('Guess what the Secret Word is: ')

# Creating a condition using the while keyword
while guess != secret_word:
    print('Oops!Wrong guess. Try again')
    guess = input('Try a new guess!: ')
print('Yaay! You got it. Great job')    
