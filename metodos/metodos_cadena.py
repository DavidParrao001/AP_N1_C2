nombre_personal = 'David Parra'
titulo_personal = 'Desarrollador . Net Fullstack'
ciudad = 'TEMUCO'

#cadena_texto = 'esto es una cadena de texto'

#el método DIR, nos indica todos los métodos disponible para la variable
#print(dir(nombre_personal))

print(f'Su nombre personal CAPITALISMO: {nombre_personal.capitalize()}')
print(f'Su nombre personal MAYÚSCULAS: {nombre_personal.upper()}')
print(f'Su nombre personal como TÍTULO: {nombre_personal.title()}')
print(f'Ciudad en MINÚSCULAS: {ciudad.lower()}')
print(titulo_personal.count('e'))
print(titulo_personal.count('x'))

print(titulo_personal.find('llador'))
print(titulo_personal.index('llador'))
