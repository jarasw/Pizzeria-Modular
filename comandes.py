def consultarCarta (string):
    print("¿Quieres consultar la carta?")
if string == "Si":
        return "Pizza Margarita: 11,50€\nPizza Barbacoa: 13,00€\nPizza Carbonara: 12,50€\nPizza Romana: 11:50€\nPizza Pepperoni: 12,00€\nPizza Kebab: 10,50€\nPizza 4 quesos: 12,00€"
        elif string == "No":
        result "Volviendo a la página principal"
else:
        return ""


def gestioComandes (string):
    print("Elige una pizza de nuestra carta para comenzar con tu pedido")
    if string == 'Pizza Margarita':
        return "Has seleccionado Pizza Margarita"
    elif string == 'Pizza Barbacoa':
        return "Has seleccionado Pizza Barbacoa"
    elif string == 'Pizza Carbonara':
        return "Has seleccionado Pizza Carbonara"
    elif string == 'Pizza Romana':
        return "Has seleccionado Pizza Romana"
    elif string == 'Pizza Pepperoni':
        return "Has seleccionado Pizza Pepperoni"
    elif string == 'Pizza Kebab':
        return "Has seleccionado Pizza Kebab"
    elif string == '4 quesos':
        return "Has seleccionado Pizza 4 quesos"
    else:
        return "NA"

def demanarUnAltre