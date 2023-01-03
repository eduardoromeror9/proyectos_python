
def busqueda_binaria(lista, elemento):
  izquierda = 0
  derecha = len(lista) - 1
  while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    if lista[medio] == elemento:
      return medio
    elif lista[medio] > elemento:
      derecha = medio - 1
    else:
      izquierda = medio + 1
  return -1

# Prueba de la función
print(busqueda_binaria([1, 2, 3, 4, 5], 3))
print(busqueda_binaria([1, 2, 3, 4, 5], 6))