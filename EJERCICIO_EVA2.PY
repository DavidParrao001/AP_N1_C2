# Los ejercicios a resolver deben incluirse dentro de un menú
# mediante el cual se ejecutará cada uno de ellos.

# 1.- Escriba una función que al ser llamada imprima el saludo "Buen día!"
def saludos_quetal ():
   mensaje = 'muy buenos dias'
   return mensaje

# 2.- Escriba una función que solicite al usuario ingresar su nombre
# en una variable nombre_usuario
# y al ser llamada imprima el saludo "Buen día 'nombre_usuario'!"
def Nombre_xd():
    nombre_usuario = solicitar_nombre()
    saludo_1 = 
    return mensaje

def solicitar_nombre():
    nombre_usario = input ('ingrese su nombre: ')
    return Nombre_xd

 
# 3.- Escribir una función que pida al usuario un número entero menor a 10
# y al ser llamada entregue el factorial de ese número


def menu_principal():
    while True:
        print()
        print('[1] en la mañana')
        print('[2] Ejercicio 2')
        print('[3] Ejercicio 3')
        print('[0] Salir')

        opcion = input('Ingrese su Opción [0-3]')
        valores_opcion = ['0','1','2','3']

        if opcion in valores_opcion:
            if opcion == '1':
                respuesta = saludos_quetal ()
            elif opcion == '2':
                pass
            elif opcion == '3':
                pass
            elif opcion == '0':
                print('Saliendo del sistema...')
                break
            print()
            print (respuesta)
        else:
            print('Opción ingresada NO corresponde...')

menu_principal()