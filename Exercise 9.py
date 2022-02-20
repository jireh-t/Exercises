#Number Printing Exercise


for num in range (0, 1000001, 100):
    print(num)

#Input Number Exercise
num = int(input("What number should I count to?"))
for num in range (0, num + 1):
    print(num)

#Random Exercise
number = random.randint(1, 5)
guess = int(input("What is the number???"))
while guess != number:
    if guess < number:
        print("Guess Higher")
        guess = int(input("What is the number???"))
    else:
        print("Guess Lower")
        guess = int(input("What is the number???")




