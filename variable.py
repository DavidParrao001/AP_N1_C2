saludo = 'Buen día querido '
nombre = input('Ingrese su nombre: ')
print()
print(saludo + nombre)

# Ingrese 2 números mediante su teclado y muestre el resultado de la suma
print('Vamos a sumar 2 números enteros')
numero_1 = 0
numero_2 = 0
resultado = 0

# Convirtiendo los textos ingresados en NÚMEROS
numero_1 = int(input('Ingrese el primer número entero: '))
numero_2 = int(input('Ingrese el segundo número entero: '))

# Después de convertir a número, viene la operación aritmética
resultado = numero_1 + numero_2

# Mostramos el resultado, para cooncatenar el número de la variable resultado, lo convertimos en texto
print('El resultado de la suma es: ' + str(resultado))

# Concatenación FORMATEANDO como cadena de texto
print(f'El resultado de la suma es: {resultado}')
print(f'{numero_1} + {numero_2} = {resultado}')