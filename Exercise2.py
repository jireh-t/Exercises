name = input("Enter name: ")
age = int(input("Enter age: "))
print("Hi {}, you are {}".format(name, age))

#Tell user how old they will be in 5 years
print("In 5 years time, you will be", age + 5)

food= input("What is your favourite food?")
print(f"Yummmm now I want {food}")

print("Now for a quiz, ...")
my_age=input("What is my age?")
if my_age == "14":
    print("You are correct!!")
else:
    print("NOPEEEEEEEEEE")

print("That is the end of the quiz")
a=input("Please enter your name one more time: ")
print("Bye!", a.upper())
