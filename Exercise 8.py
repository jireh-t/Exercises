#Average Exeercise
number_of_items = int(input("How many numbers to average?"))
count = 0
total = 0
while count < number_of_items:
    count += 1
    number = int(input(f"Enter number {count}: "))
    total += number
print(f"Total is {total}")
print(f"Average is {total/number_of_items}")

