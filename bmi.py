def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight/(height**2)
    print(f"BMI = {BMI}")
    if BMI < 18.5:
        print("Underweight")
    elif BMI <= 24.9:
        print("Normal")
    elif BMI <= 29.9:
        print("Overweight")
    else:
        print("Obese")

calculate_bmi(weight=70, height=1.78)
