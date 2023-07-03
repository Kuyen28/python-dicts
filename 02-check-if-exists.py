english_to_spanish = {"one":"uno", "two":"dos"} # Crea un diccionario con dos elementos

# Podemos revisar si cierta llave está presente en el diccionario con la palabra reservada in

if "one" in english_to_spanish:
    print("Si está la llave one")
    print("Su valor es:", english_to_spanish["one"])

# Si tratamos de acceder a una llave que no existe, cometeremos un error de llave

# print(english_to_spanish["Three"])