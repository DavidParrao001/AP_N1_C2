
import math
from calculadora import convertir_float

def area_circulo(Radio):
   resultado = PI * Radio**2
   print(f'el area del circulo es = {resultado}')
   return
        
def volumen_cilindro(altura,Radio):
    area = area_circulo(Radio)
    resultado = Radio * altura
    return

def calculo_cilindro():
   print('Ingrese los datos solicitados')
   str_radio = input("radio de cilindro: ")
   str_radio = input("volumen de cilindro: ")
   radio = calculadora.convertir_float(str_radio)
   altura = calculadora.convertir_float(str_radio)
   volumen = volumen_cilindro(radio,altura)
   print(volumen)




print("-----------------------------------------------------------")
print("calculadora de area de circulo y volumen de cilindro")
print("===================================================")

print ("holaa, que vas a querer hacer el dia de hoy?")
while True:
 print('[1] calcular area de un circulo')
 print('[2] calcular el volumen')
 opcion = input('\nSeleccione su operación [0-2]: ')

 if opcion == '1':
    calculo_cilindro
 elif opcion == '2':
    area_circulo(Radio)

 else:
    print('Opción NO válida.')