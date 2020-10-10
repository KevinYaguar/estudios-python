import sys

try:
    numero1 = int(input('Ingrese numero 1: '))
    numero2 = int(input('Ingrese numero 2: '))
except ValueError:
    print('Valor no válido')
    sys.exit(1)

try:
    resultado = numero1 / numero2
    error = 0
except ZeroDivisionError:
    print('No se puede dividir por zero')
    error = 1
else:
    print('Todo salio bien')
finally:
    print(f'Error = {error}')
    

print(f'El resultado de la operacion {numero1}/{numero2}={resultado}')