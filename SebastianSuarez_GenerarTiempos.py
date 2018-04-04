import numpy as np
import time

#Se define la funcion de fibonacci

def fibonacci(N):

	#Caso1
	if (N == 1 or N==0):
		return N

	#caso recursivo
	else:
		return fibonacci(N-1) + fibonacci(N-2)

#Pruebas
#print fibonacci(0)
#print fibonacci(5)
#print fibonacci(10)

t0 = time.time()

#Se define la funcion que toma el tiempo que tarda en devolver el valor(N) de la serie de fibonacci

def get_time(N):

# SOME CODE THAT TAKES TIME
	fibonacci(N)
	t1 = time.time()-t0

	return t1

#Se imprime el valor (N) de la serie de fibonacci y el tiempo que tarda en devolver este valor la funcion

print fibonacci(35), get_time(35)
