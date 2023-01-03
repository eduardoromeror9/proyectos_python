def replace_word():
    palabra = 'hola hola, hola de prueba y quiero cambiar las palabras'
    palabra_a_cambiar = input('Ingrese la palabra a cambiar: ')
    palabra_nueva = input('Ingrese la palabra nueva: ')
    print(palabra.replace(palabra_a_cambiar, palabra_nueva)) # Reemplaza la palabra ingresada por la nueva con el metodo replace()

replace_word()