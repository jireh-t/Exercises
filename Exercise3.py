GST= 0.15
item = float(input("Enter item price"))
item_GST = item * GST
total_cost = item + item_GST
print(f"total cost ${total_cost}")

num = int(input("Number of gigabytes?"))
multiplier = 1024
print(f"Your number of megabytes is {num * multiplier}")


