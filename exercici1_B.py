
def funcion3():
    while True:
        edad = input("¿Que edad tienes?")
        if edad.isnumeric():
            break
    edad = int(edad)
    year = 2023
    a = year - edad
    print("Este es tu año de nacimiento:", a)
funcion3()