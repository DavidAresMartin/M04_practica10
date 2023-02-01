

def funcion1():
    año = int(input("Año de nacimiento:"))
    #Aquí estoy asignando que cuando un int al imput porque sino lo detecta como un String
    añoActual = int(input("Año actual: "))
    edad = añoActual - año
    Resultado = "en este año {} tiene {}".format(añoActual, edad)
    #La función format permite incluir en una cadena, texto y caracteres de formateo,
    # que representan un tipo en particular de datos, tales como entero, cadena o flotante
    return print(Resultado)

