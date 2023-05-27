import random

print("Welcome to my Number Guessing Game!")
#Get max number for guess
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a number")
    quit()

#Generate random number 0-10
random_number = random.randint(0,top_of_range)
guesses = 0

#Guess number
while True:
    guesses += 1
    user_guess = input("Guess a number between 0 and " + str(top_of_range) + ".")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number")
        continue

    if user_guess == random_number:
        print("You got it!!")
        break
    elif user_guess > random_number:
        print("Too high!")
    else:
        print("Too low!")
        
#Print how many guesses it took
print("You got it in", guesses, "guesses")
