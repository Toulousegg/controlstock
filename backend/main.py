from turtles import *

dimesiones = input('Escribe las dimesiones de la chapa: ')
separador = 'x'
dim_sep = dimesiones.split(separador)
veio = input('Escribe la dirección del veio: ')
veioint = int(veio)

def grafico():
	#cuantas veces va a girar
	for i in range(2):
		forward(60)
		rigth(90)
		forward(100)
		rigth(90)

def grafico2():
	for i2 in range (2):
		forward(60)
		rigth(90)
		forward(100)
		rigth(90)
		forward(25)
		rigth(90)
		forward(25)
		rigth(90)
		forward(25)
		rigth(90)
		forward(25)
		rigth(90)
		forward(25)
		rigth(90)
		forward(25)
		rigth(90)
		forward(25)
		rigth(90)
		forward(25)

if veio == dim_sep[0]:
	print(f'el veio apunta hacia {dim_sep[0]}')
	grafico()

else:
	print(f'EL veio esta apuntando hacia{dim_sep[1]}')
	grafico2()

if veio == None:
	print('Pieza sin veio')

input('Presiona enter para salir')