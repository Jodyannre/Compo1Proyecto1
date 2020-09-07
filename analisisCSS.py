
class CSS:
	textoEntrante = ""
	def __init__(self, textoEntrante):
		self.textoEntrante = textoEntrante

	def ejecutar(self):
		estado = 0
		for i in self.textoEntrante.lower():
			if estado == 0:	
				if i == '/': #es comentario unilinea o multilinea.
					estado = 1
			elif estado == 1:
				if i == '*': #es comentario unilinea o multilinea
					estado = 2
			elif estado == 2:
				if i == '/':
					estado = 3 #es posiblemente fin de comentario.
				else:
					estado = 2
			elif estado == 3:
				if i == '*': #es posiblemente fin del comentario.
					estado = 4
			elif estado == 4:
				if i == '\n': #sí es salto de línea se acepta que es comentario unilinea
					estado = 5
				else:
					estado = 2 #sino regresa y sigue reconociendo dentro de comentario
			elif estado == 5: #estado de aceptación para comentario unilínea
				estado = 0