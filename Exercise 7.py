#Number Exercise
number = 0
while number <= 10:
    print(number)
    number += 1
print("All done!")


#Number Down Exercise
number = 10
while number > -2:
    print(number)
    number -= 2
print("YAY!!!")


#Fizz, Buzz Exercise
number = 0
while number <= 100:
    if number %5 == 0 and number %3 == 0:
        print("FIZZBUZZ")
    elif number %3 == 0:
        print("FIZZ")
    elif number %5 == 0:
        print("BUZZ")
    else:
        print(number)
    number += 1


#Password Exercise
word = input("What is the password?")
PASSWORD = "noodles"
GUESS = 2
while word != PASSWORD and GUESS > 0:
    print("Password incorrect! Try again!")
    GUESS -= 1
    word = input("What is the password?")
while GUESS == 0 and word != PASSWORD:
    print("no more guesses, too many attempts")
    break
while word == PASSWORD:
    print("Access Granted!!!!")
    break






