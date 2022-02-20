#Exam Marks Exercise

num = int(input("what is your mark?"))
if num >= 90 and num <=100:
    print("Well done!!! You got an A")
elif num >= 70 and num <= 89:
    print("better luck next time, you got a B")
elif num >= 50 and num <= 69:
    print("A little study wouldn't hurt, you got C")
elif num < 50:
    print("FAIL, You need to study next time")
else:
    print("I don't know what test you took, it was only out of 100!")


#Paracetemol Exercise
P_AGE = 12
P_WEIGHT = 10
age = int(input("What is your age?"))
if age < P_AGE:
    weight = int(input("What is your weight in kgs?"))
    print(f"Recommend {weight*P_WEIGHT}mg of paracetemol")
if age >= 12:
    print("Please have 2 500mg tablets")


#Alarm Exercise (Words)
week_day = 'monday' or 'tuesday' or 'wednesday' or 'thursday' or 'friday'
saturday = 'saturday'
sunday = 'sunday'
day = input("what is the day")

week_day = week_day.lower()
if day == week_day:
    print("alarm rings at 7")
elif day == saturday:
    print("alarm rings at 8")
elif day == sunday:
    print("alarm tings at 9")
else:
    print("THAT'S NOT A DAY OF THE WEEK!")


#Alarm Exercise (Numbers)
day = int(input("what day is it (1 = monday.....7 = sunday)?"))
if day <= 5:
    print("alarm rings at 7")
elif day == 6:
    print("alarm rings at 8")
elif day == 7:
    print("alarm rings at 9")
else:
    print("THAT IS NOT A DAY OF THE WEEK!")

#Leap year Exercise
year = int(input("What year is it?"))
if year %4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")



