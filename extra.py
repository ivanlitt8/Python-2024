# Módulo agregar al inventario
def agregar_producto(inventario):
  nombre = input("Ingrese el nombre del producto: ")
  cantidad = int(input("Ingrese cantidad: "))
  if nombre in inventario:
    # Si art existe acumula la cantidad en el art
    inventario[nombre] = inventario[nombre] + cantidad
    print(f"'{nombre}' sumado correctamente.")
  else:
    # Si art no existe lo crea asignando cantidad
    inventario[nombre] = cantidad
    print(f"'{nombre}' agregado correctamente.")
    
# Módulo eliminar de inventario
def eliminar_producto(inventario):
  nombre = input("Nombre del producto a eliminar: ")
  if nombre not in inventario: # El nombre de art  no existe
    print(f"El producto '{nombre}' no existe en el inventario.")
  else:
    del inventario[nombre] # El art se elimina del diccionario
    print(f"Producto '{nombre}' eliminado correctamente.")
    
# Módulo impresión inventario
def mostrar_inventario(inventario):
  print("-" * 16)
  print("Inventario actual:")
  for nombre, cantidad in inventario.items():
    print(f"{nombre}: {cantidad}")
  print("-" * 16)

def main():
  # Diccionario vacío
  inventario = {}   
  # Ejecucion hasta el 'break'
  while True:
    # Impresion menú
    print("-" * 8)
    print("Opciones:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir de programa")
    print("-" * 8)

    # Selección
    opcion = int(input("Seleccione una opción: "))

    # Funciones según opción
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
      print("La opción seleccionada es inválida") # Funcion fuera de rango

main()
