import random
from logo_art import logo
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_chosen):
  if level_chosen=='easy':
    return EASY_LEVEL_ATTEMPTS
  else:
    return HARD_LEVEL_ATTEMPTS
def check_answer(guessed_number,answer,attempts):
  if guessed_number<answer:
    print("your guess is too low")
    return attempts-1
  elif guessed_number >answer:
    print("your guess is to high")
    return attempts
  else:
    print(f"your guess is right...The answer was {answer}")
def game():
  print(logo)
  print("let me think of a number 1 to 50.")
  answer=random.randint(1,50)
  print(answer)
  level=int(input("Choose level difficulty...Type 'easy' or 'hard':"))
  attempts=set_difficulty(level)
  guessed_number=0
  while guessed_number!=answer:
    print(f"you have {attempts} remaining to guess the number.")
    guessed_number=int(input("Guess a number:"))
    attempts=check_answer(guessed_number,answer,attempts)
    if attempts == 0:
      print("out of guesses")
      return
    elif guessed_number!= answer:
      print("Guess again")

game()
  