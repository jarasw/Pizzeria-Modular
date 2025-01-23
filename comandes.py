def consultarCarta(string):
    print("¿Quieres consultar la carta?")
    if string == "Si":
        return (
            "Pizza Margarita: 11,50€\n"
            "Pizza Barbacoa: 13,00€\n"
            "Pizza Carbonara: 12,50€\n"
            "Pizza Romana: 11,50€\n"
            "Pizza Pepperoni: 12,00€\n"
            "Pizza Kebab: 10,50€\n"
            "Pizza 4 quesos: 12,00€"
        )
    elif string == "No":
        return "Volviendo a la página principal"
    else:
        return "Opción no válida, por favor responde 'Si' o 'No'"


def gestioComandes():
    print("Elige una pizza de nuestra carta para comenzar con tu pedido")
    carta = {
        'Pizza Margarita': 11.50,
        'Pizza Barbacoa': 13.00,
        'Pizza Carbonara': 12.50,
        'Pizza Romana': 11.50,
        'Pizza Pepperoni': 12.00,
        'Pizza Kebab': 10.50,
        'Pizza 4 quesos': 12.00
    }
    
    pedido = []
    
    while True:
        print("\nCarta de pizzas:")
        for pizza, precio in carta.items():
            print(f"- {pizza}: {precio:.2f}€")

        seleccion = input("Escribe el nombre de la pizza que deseas pedir: ")
        
        if seleccion in carta:
            pedido.append(seleccion)
            print(f"Has seleccionado {seleccion}")
        else:
            print("La pizza seleccionada no está en la carta. Intenta nuevamente.")

        otra = input("¿Quieres pedir otra pizza? (Si/No): ").strip().lower()
        if otra != "si":
            break

    if pedido:
        print("\nTu pedido final:")
        for pizza in pedido:
            print(f"- {pizza}")
        print(f"Total: {sum(carta[p] for p in pedido):.2f}€")
    else:
        print("No has realizado ningún pedido.")