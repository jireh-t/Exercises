km=int(input("How many kilometers??"))
miles = km*0.621371
print("Equivalent miles:", miles)

#Eggs exercise
eggs = int(input("How many eggs?"))
bdozen= eggs//13
print("Baker's dozen:", bdozen)
if bdozen >= 5:
    print("Wow that's a lot of eggs!")
elif bdozen <= 0:
    print("no cakes for youUUUuuu XD")
else:
    print(f"you can only make a few cakes with {bdozen} dozen eggs")

#Driving license exercise
DRIVING_AGE = 16
age=int(input("What is your age?"))
if age >= DRIVING_AGE:
    print("You can get your learner's, yay!")
else:
    print("Sorry, you are too young haha")

#Fever exercise
H_TEMP = 37
age = int(input("what is your age?"))
temp= float(input("what is your temperature?"))
if temp > 39.5:
    print("HIGH FEVER")
elif age < 2 and temp >= 38:
    print("Call Doctor")
elif H_TEMP == 37:
    print("you are healthy and normal")

#Giving Blood Exercise
B_AGE= 16
B_WEIGHT= 50
age = int(input("how old are you?"))
weight = int(input("What is your weight in Kgs?"))
if age >= B_AGE and weight >= B_WEIGHT:
    print("You can give your blood to people")
elif age < B_AGE and weight < B_WEIGHT:
    print("nope you can't give blood")
elif age < B_AGE:
    print("sorry you are too young")
elif weight < B_WEIGHT:
    print("sorry you are to light")

#Even Exercise
number = int(input("give me a number:"))
if number % 2 == 0:
    print("your number is even")
else:
    print("your number is odd")
