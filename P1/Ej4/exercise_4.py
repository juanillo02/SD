# Exercise 4 Template
import os

# Do not modify the file name or function header
# Return the size of the file and words ending in 's'
def get_file_info(filename):
	size = 0
	# Lista donde vamos a guardar las palabras terminadas en "s"
	wordlist = []
	# Lista donde vamos a guardar las palabras del fichero
	lista2 = []
	# Cuando el fichero esta vacio o no es una cadena, salta el TypeError
	if type(filename) is None:
		raise TypeError("Nulo")
	if type(filename) is not str:
		raise TypeError("No es una cadena")
	# Abrimos el fichero para leer su contenido
	try:
		with open(filename, 'r') as f:
			# El comando sirve para saber el tamano de bytes de la lista, y los guardamos en la variable size
			size = os.path.getsize(filename)
			# Lee el contenido del fichero
			for linea in f:
				# Divide el contenido del fichero por palabras y guarda cada palabra como un elemento de la lista2
				lista2.extend(linea.split())
				n = lista2
				# Lee cada palabra y mira cuanto es la longitud de cada una
				for i in range(0, len(n)):
					# Si cada palabra tiene una longitud, al restar 1, sabemos en que posicion se encuentra la ultima letra.
					# Entonces, si esa palabra termina en "s", la guardamos en wordlist
					if n[i][len(n[i])-1] == 's':
						wordlist.append(n[i])
	except OSError:
		print ("El fichero no existe")
	# Devuelve el tamano de bytes y las palabras terminadas en "s"
	return (size, wordlist)
