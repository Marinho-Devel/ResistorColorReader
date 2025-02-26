
#Apresentetion
print("RESISTOR COLOR CALCULATOR:")
print("Choice option: 1 for calculate by colors or 2 to get color by value")

#
def colors():
    return ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'grey', 'white', 'silver', 'gold']


def colorsCalc():
    """ Calcula o valor do resistor baseado nas cores inseridas. """
    colorsValues = colors()
    stripe = []  # List to storage the insert colors
    stripeValue = []  # List to storage the values of bands
    resistance = 0

    # Pedir os três primeiros anéis
    for i in range(3):
        color = input(f"Insert the color of stripe {i + 1}: ").lower()
        if color in colorsValues:
            stripe.append(color)
            stripeValue.append(colorsValues.index(color))
        else:
            print("Invalid color. Try again.")
            return  # Sai da função se a cor for inválida

    # Quarta listra (tolerância ou continuação)
    color = input("Insert the color of the fourth stripe: ").lower()
    if color in colorsValues:
        stripe.append(color)
    else:
        print("Invalid color. Try again.")
        return

    # Verifica se é um resistor de 4 bandas
    if color in ("gold", "silver"):
        tolerance = 5 if color == "silver" else 10  # 5% para prata, 10% para ouro
        num_bands = 4
    else:
        # Se a quarta listra não for tolerância, continua para a quinta listra
        color = input("Insert the color of the fifth stripe: ").lower()
        if color in colorsValues:
            stripe.append(color)
            stripeValue.append(colorsValues.index(color))
            num_bands = 5
        else:
            print("Invalid color. Try again.")
            return

        # Se a quinta listra não for tolerância, existe uma sexta listra (coeficiente de temperatura)
        if color not in ("gold", "silver"):
            color = input("Insert the color of the sixth stripe: ").lower()
            if color in colorsValues:
                stripe.append(color)
                stripeValue.append(colorsValues.index(color))
                num_bands = 6
            else:
                print("Invalid color. Try again.")
                return

    # Calcula a resistência
    resistance = (stripeValue[0] * 10) + stripeValue[1]
    resistance *= (10 ** stripeValue[2])

    # Exibe o resultado
    print("\n==== RESISTOR RESULT ====")
    print(f"Number of Bands: {num_bands}")
    print(f"Resistance: {resistance} Ohms")

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





