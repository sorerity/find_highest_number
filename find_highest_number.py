variable1 = int(input("Input variable number 1: "))
variable2 = int(input("Input variable number 2: "))
variable3 = int(input("Input variable number 3: "))
variable4 = int(input("Input variable number 4: "))
variable5 = int(input("Input variable number 5: "))

def find_highest_number (variable1, variable2, variable3, variable4, variable5):
    if variable1 >= variable2 and variable1 >= variable3 and variable1 >= variable4 and variable1 >= variable5:
        print ("The highest variable is variable 1: ", variable1)
    elif variable2 >= variable1 and variable2 >= variable3 and variable2 >= variable4 and variable2 >= variable5:
        print ("The highest variable is variable 2: ", variable2)
    elif variable3 >= variable1 and variable3 >= variable2 and variable3 >= variable4 and variable3 >= variable5:
        print("The highest variable is variable 3: ", variable3)
    elif variable4 >= variable1 and variable4 >= variable2 and variable4 >= variable3 and variable4 >= variable5:
        print("The highest variable is variable 4: ", variable4)
    else:
        print("The highest variable is variable 5: ", variable5)
