try:
    age = int(input("Please enter your age: "))
    if age % 2 == 0:
        print("The age you entered is even")
    else:
        print("The age you entered is odd")
except ValueError as er:
    print("You didn't enter an integer, so you get an error message saying:", er)