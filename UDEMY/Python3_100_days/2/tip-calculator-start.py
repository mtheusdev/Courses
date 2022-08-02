print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What a percentage tip would you like to give? 10, 12, or 15? "))
split_bill = int(input("How many people to split the bill? "))

result = round(((total_bill * (percentage / 100 )) + total_bill), 2) / split_bill

print(f"Each person should pay: {result}")
