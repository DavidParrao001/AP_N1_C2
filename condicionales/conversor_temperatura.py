#Teniendo 3 escalas de temperatura (Celsius, farenheit, kelvin)
#Cree un conversor de temperatura que la pida al usuario la temperatura y escala incial
# y la escala a la que desea convertir, luego muestre el resultado de la conversion

# °C a F = 1,8°c + 32°
# F a °C = 5/9 (°F-32°)

# °C a K = °C + 273°
# K a °C = K - 273°

# K a F = (1,8°C + 32°) + 273°
# F a K = (5/9(°F-32°)) + 273°
print("Sistema conversor de Temperatura")
print("==================")
print("para comenzar ingrese su escala inicial")
print("C - para Celsius")
print("F - para farenheit")
print("K - kelvin")

print ("hola, quieres usar esta calculadora")

respuesta_1 = input("si o no: ")

if respuesta_1 == "si":
    print("genial, entonces dime que vas a calcular" )

elif respuesta_1 == "no":
    print("Oh, qué lástima.")

escala_inicial = input("Ingrese escala inicial: ")
str_temperatura = input("ingrese su temperatura")
escala_final = input("ingrese escala final")

if str_temperatura.isdigit():
    temperatura = float (str_temperatura)

else:
    print("El valor de temperatura no responde")

if escala_inicial.upper == "F":
   if escala_final.upper == "K":
       pass
   if escala_final.upper == "c":
       pass
   
if escala_inicial.upper == "C":
   if escala_final.upper == "K":
       pass
   if escala_final.upper == "F":
       pass
if escala_inicial.upper == "K": 
   if escala_final.upper == "C":
       pass
   if escala_final.upper == "F":
       pass
   pass
else:
    print("Escala incial No corresponde.")