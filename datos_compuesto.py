# Las LISTAS son colecciones ordenadas y mutables,
# es decir, son modificables una vez creadas.
# Pueden almacenar elementos de diferentes tipos al mismo tiempo,
# ideales para almacenar una colección de datos que necesita ser modificada o accedida por índices.
# Almacena los datos en 2 espacios de memoria, el índice y el dato mismo.

print("\nTrabajando con LISTAS.\n======================")
lista = ["Armando Casas", True, 1.73]
print(lista)

print(type(lista))

print(lista[0])
print(lista[1])
print(lista[2])

print(type(lista[0]))
print(type(lista[1]))
print(type(lista[2]))


str_nombre = input ('ingrese su nombre')
lista [0]= str_nombre #cambio valido, acceso al elemento por ÍNDICE
print (lista[0])


#reemplace el primer elemento de la lista por su edad

edad = int  (input ('ingrese su edad'))
lista [1]= edad #cambio valido, acceso al elemento por ÍNDICE
print (lista[1])

#los DICCIONARIOS con colecciones no ordenadas de pares KEY: VALUE, usando 2 espacio de memoria.
#permiten almacenar datos de manera que cada elemento pueda ser recuperado, actualizado o eliminado usando su clave.

