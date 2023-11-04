# Exercise 3 Template

# Do not modify the file name or function header

# Retuns a list with the prime numbers in the [a, b] interval
def prime(a, b):
	# En esta lista se van a guardar los numeros que son primos
	primes = []
	# Este bucle recorre los numeros que se encuentran entre a y b, incluido el a y el b.
	for n in range(a, b+1):
		# El contador se inicializa
		c = 0
		# Este bucle recorre desde 2 hasta n, siendo n la posicion i del vector.
		for d in range(2, n):
			# Si el resto de dividir n entre d es cero, entonces al contador se le suma uno
			if n % d == 0:
				c += 1
		# Si el contador es 0, se anade a la lista primes los valores primos
		if c == 0:
			primes.append(n)
	# El tipo de a es nulo o no es entero, entonces salta el TypeError
	if type(a) is None:
		raise TypeError("Nulo")
	if type(a) is not int:
		raise TypeError("No es entero")
	# El tipo de b es nulo o no es entero, entonces salta el TypeError
	if type(b) is None:
		raise TypeError("Nulo")
	if type(b) is not int:
		raise TypeError("No es entero")

	return primes
