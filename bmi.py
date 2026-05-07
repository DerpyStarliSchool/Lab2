def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight/(height**2)
    print(f"BMI = {BMI}")
    if BMI < 18.5:
        print("Underweight")
        test = -1
        return test
    elif BMI <= 24.9:
        print("Normal")
        test = 0
        return test
    elif BMI <= 29.9:
        print("Overweight")
        test = 1
        return test
    else:
        print("Obese")
        test = 2
        return test

result = calculate_bmi(weight=70, height=1.78)
