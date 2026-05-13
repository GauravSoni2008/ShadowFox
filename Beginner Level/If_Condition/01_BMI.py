height = float(input("Enter height in meters: "))
wieght = float(input("Enter weight in kilograms: "))
BMI = wieght/height**2
print(f"BMI: {BMI:.2f}")
if BMI >= 30:
    print("Obesity")

elif BMI >= 25:
    print("Overweight")

elif BMI >= 18.5:
    print("Normal")

else:
    print("Underweight")