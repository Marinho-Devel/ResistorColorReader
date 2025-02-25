print("RESISTOR COLOR CALCULATOR:")
print("Choice option: 1 for calculate by colors or 2 to get color by value")

def colors():
    return ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'grey', 'white']

def colorsCalc():
    #tolerance = ['silver', 'gold']
    colorsValues = colors()         #ASSINGS THE RETURN VALUE OF A FUNCTION TO A VARIABLE
    stripe = [1, 2, 3, 4]
    resistorValue = [1, 2, 3, 4]
    resistence = 0
    for i in range(len(stripe)):
        stripe[i] = input(f"insert the color of {stripe[i]} stripe: ")

        if stripe[i] in colorsValues:
            resistorValue[i] = colorsValues.index(stripe[i])
        else:
            print("invalid color.")

    resistence = (resistorValue[0] * 10) + resistorValue[1]
    resistence = resistence * (10 ** resistorValue[2])
    print("the resistence in Ohms is:", resistence)
    print("resistor value:", resistorValue)



    print(f"color: {colorsValues[2]}")

def valueCalc(colorsValues):
    print(f"color: {colorsValues[3]}")

def menu():
    choice = input("insert the option: ")

    match choice:

        case '1':
            colorsCalc()

        case '2':
            valueCalc()

        case '3':
            print("exiting")

        case _:
            print("invalid option.")

menu()





