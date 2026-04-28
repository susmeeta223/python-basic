import random
random_number = random.randint(1, 100)

#print(random_number)
attempts = 10

print("Welcome to the number guessing game")
print(f"I am thinking of a number between 1 to 100. You have {attempts} attempts")

while attempts > 0:
    guess_number = input("Guess the number: ")

    try:
        guess_number = int(guess_number)
    except ValueError:
        print("Invalid input, please input valid number")
        continue

    if guess_number < random_number:
        print("Too low , try again with higher number")
    elif guess_number > random_number:
        print("Too high, try again with lower number")
    else:
        print(f"Congratulation, you have guess the number {random_number} correctly")
        break

    attempts -= 1
    print(f"You have {attempts} attempts left")

if attempts == 0 :
    print(f"Game over, the number was thinking of was: {random_number}")




