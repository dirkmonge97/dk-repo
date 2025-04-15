
import random
secret_number = random.randint(1,10)
guess = int(input("Type the secret number from 1 to 10:"))
while guess != secret_number:
    guess = int(input("Type the secret number from 1 to 10:"))
    if guess == secret_number:
        continue
print ("you guessed the secret number")

