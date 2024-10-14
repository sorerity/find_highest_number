variable1 = int(input("Input variable number 1: "))
variable2 = int(input("Input variable number 2: "))
variable3 = int(input("Input variable number 3: "))
variable4 = int(input("Input variable number 4: "))
variable5 = int(input("Input variable number 5: "))

def find_highest_number (variable1, variable2, variable3, variable4, variable5):
    if variable1>variable2:
        if variable1>variable3:
            if variable1>variable4:
                if variable1>variable5:
                    print("Variable 1 is the Highest:", variable1)