print("RESISTOR COLOR CALCULATOR:")
print("Choice option: 1 for calculate by colors or 2 to get color by value")
choice = input("insert the option: ")
def menu():
    match choice:
        case '1':
            colorsCalc()

        case '2':
            valueCalc()

        case _:
            print("invalid option.")

    menu()

def dictionary():
    colorsValues = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'purple': 7, 'grey': 8, 'white': 9}
    return colorsValues

def colorsCalc(colorsValues):
    print(f"color: {colorsValues[2]}")

def valueCalc(colorsValues):
    print(f"colof: {colorsValues[3]}")

