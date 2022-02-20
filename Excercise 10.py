import random
number = random.randint(1, 5)
guess = int(input("What is the number???"))
while guess != number:
    if guess < number:
        print("Guess Higher")
        guess = int(input("What is the number???"))
    else:
        print("Guess Lower")
        guess = int(input("What is the number???")
print("CORRECT")
