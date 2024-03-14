def agregar_producto(inventario):
  nombre = input("Ingrese el nombre del producto: ")
  cantidad = int(input("Ingrese la cantidad: "))
  if nombre in inventario:
    inventario[nombre] = inventario[nombre] + cantidad
    print(f"'{nombre}' sumado correctamente.")
  else:
    inventario[nombre] = cantidad
    print(f"'{nombre}' agregado correctamente.")

def eliminar_producto(inventario):
  nombre = input("Nombre del producto a eliminar: ")
  if nombre not in inventario:
    print(f"El producto '{nombre}' no existe en el inventario.")
  else:
    del inventario[nombre]
    print(f"Producto '{nombre}' eliminado correctamente.")

def mostrar_inventario(inventario):
  print("-" * 20)
  print("Inventario actual:")
  for nombre, cantidad in inventario.items():
    print(f"{nombre}: {cantidad}")
  print("-" * 20)

def main():
  inventario = {}
  while True:
    print("-" * 20)
    print("Opciones:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir")
    print("-" * 20)

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
      agregar_producto(inventario)
    elif opcion == 2:
      eliminar_producto(inventario)
    elif opcion == 3:
      mostrar_inventario(inventario)
    elif opcion == 4:
      print("Inventario cerrado")
      break
    else:
      print("La opción seleccionada es inválida")

main()
