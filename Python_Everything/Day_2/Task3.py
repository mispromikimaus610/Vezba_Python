import random
random: int = random.randint(1,10)
guess:int = int(input("Guess the number: "))
if guess == random:
    print("You guessed it right!")
else:
    print(f"You guessed it wrong! The number was {random}")