import random
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
secret_number = random.randint(start, end)
print("Guess the number!")
guess = 0
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess > secret_number:
        print("Too High!")
    elif guess < secret_number:
        print("Too Low!")
    else:
        print("Correct! You guessed the number.")