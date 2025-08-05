import random 
num=random.randint(1,100)
print("Welcome to the Nummber guessing game!")
print("I have selected a number between 1 and 100.")
print("Can you guess what it is?")
guess_count =1
while True:
    guess=int(input("Enter your guess: "))
    if guess < num:
        print("Your guess is too low. Try again.")
    elif guess > num:
        print("Your guess is too high. Try again.")
    else:
        print("Congratulations! You guessed the number!")
        break
    guess_count += 1
print(f"You guessed the number in {guess_count} tries.")
print("Thanks for playing!")