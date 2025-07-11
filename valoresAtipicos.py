#Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3. 
#Nota: La puntuación típica de un valor se obtiene restando la media y dividiendo por la desviación típica de la muestra.

import MATH

def atipicos(muestra):

	suma = 0

	for i in range(len(muestra)):
		suma += muestra[i]

	media = suma/len(muestra)

	for i in range(len(muestra)):
		valorTipico = (muestra[i] - media)/ MATH.Deviation(muestra)
		#podria usar tambien algo asi y en ese caso la funcion anterior no haria falta
		#valor valorTipico = (muestra[i] - MATH.Media(muestra))/ MATH.Deviation(muestra)
		if valorTipico > 3 or puntuacion < -3:
			print(valorTipico)
