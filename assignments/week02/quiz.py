"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""
# BMI Calculator

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.1f}")

if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Category: Normal weight")
elif 25.0 <= bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")



"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
# Currency Converter
rate = 35.5

print("Choose conversion direction:")
print("1: THB to USD")
print("2: USD to THB")
choice = input("Enter 1 or 2: ")

amount = float(input("Enter the amount: "))

if choice == "1":
    result = amount / rate
    print(f"{amount:.2f} THB = {result:.2f} USD")
    print(f"Formula: USD = THB / {rate}")
elif choice == "2":
    result = amount * rate
    print(f"{amount:.2f} USD = {result:.2f} THB")
    print(f"Formula: THB = USD × {rate}")
else:
    print("Invalid choice. Please enter 1 or 2.")
