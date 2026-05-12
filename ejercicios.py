import math
def factorial(): 
    num = int(input("porfavor ingrese un numero menor a 10: "))

    if num < 0:
        print ("el numero debe ser positivo.")
    elif num >= 10:
        print ("el numero debe ser menor que 10.")
    else:
        resultado = math.factorial(num)
        print(f"El factorial de {numero} es {resultado}")
        factorial()