import sys
import operaciones

operations = {
    1: operaciones.sum,
    2: operaciones.substract,
    3: operaciones.multiply,
    4: operaciones.divide
  }

def pick(value, value_one, value_two):
  operation = operations.get(value, "Digite una opcion correcta")
  return operation(value_one, value_two)

exit = True
i = 0
while exit:
  print("Elige la operacion que quieres")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")
  if i != 0:
    print("5. Volver a elegir los numeros para sumar", "Nota: Esta opcion reiniciara la calculadora")
  print("0. Salir")
  operation = input()
  if int(operation) == 0:
    print("Saliendo ;)")
    sys.exit()
  if int(operation) == 5:
    i = 0
    continue
  if i == 0:
    print("Ingresa el primer valor")
    value_one = input()
    print("Ingresa el segundo valor")
    value_two = input()
  else:
    print("Ingresa el valor")
    value_two = input()
  result = pick(int(operation), int(value_one), int(value_two))
  print("El resultado es:", result)
  value_one = result
  i += 1

