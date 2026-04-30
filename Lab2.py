
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    str_numbers = input()
    str_list = str_numbers.split(",")
    float_list = []
    for num in str_list:
        float_list.append(float(num))
    print(f"The values are {float_list}")
    return float_list

def average(x):
    average = sum(x)/len(x)
    print(f"The average is {average}")

def minmax(x):
    minimum = min(x)
    maximum = max(x)
    print(f"The minimum is {minimum}")
    print(f"The maximum is {maximum}")

def median(x):
    x.sort()
    n = len(x)
    m= n//2
    if n%2 == 0:
        median = (x[m-1]+x[m])/2
    else:
        median = x[m]
    print(f"The median is {median}")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average(num_list)
    minmax(num_list)
    median(num_list)

if __name__ == "__main__":
    main()


