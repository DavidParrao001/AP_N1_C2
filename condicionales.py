
#solicite al usuario el ingreso de datos personales (nombre, edad y titulo).
#si el usuario es mayor de edad, muestre por pantalla todos sus datos.
#si el usuario no es mayor de edad, muestre un mensaje indicando que es menor de edad.

nombre = input('por favor ingrese su nombre: ')

edad = int(input("puede decir su edad: "))

titulo = input('puede ingresar su titulo: ')

 
if edad >= 18:
    #Este set de acciones de ejecuta cuando la respuesta es V
    print('usted se llama {}, es mayor de edad y tiene {} y de titulo tiene {}'.format(nombre, edad, titulo))
else:
    #Este set de acciones se ejecuta cuando la respuesta es F
    print('usted es menor de edad.')