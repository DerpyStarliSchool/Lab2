def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight/(height**2)
    print(f"BMI = {BMI}")
    if BMI < 18.5:
        print("Underweight")
        return -1
    elif BMI <= 24.9:
        print("Normal")
        return 0
    elif BMI <= 29.9:
        print("Overweight")
        return 1
    else:
        print("Obese")
        return 2

result = calculate_bmi(weight=70, height=1.78)
