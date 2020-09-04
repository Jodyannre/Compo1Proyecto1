from graphviz import Digraph

class JS:
	textoEntrante = "" #variable global que obtiene el texto a analizar.
	dot = "" #variable global para generar el .dot
	estadoAnterior = ""
	caracterAnt = ""
	def __init__(self, textoEntrante):
		pathW = textoEntrante.split('//PATHW:')
		splitear = pathW[1].split('\n')
		self.dot = Digraph('Web_editor_js',filename=splitear[0]+'//tabla.dot', format='png')
		self.dot.attr(rankdir='LR')
		self.textoEntrante = textoEntrante + "\n"

	def ejecutarDot(self):
		self.dot.render(view=True)

	def ejecucion(self):
		estado = 0
		for i in self.textoEntrante.lower():
			if estado == -1: #estado sumidero error
				print(str(estado)+"->"+i)
			if estado == 0: #estado inicial
				if i == '/': #comentarios múltiples, definición de rutas
					#print(str(estado)+"->"+i)
					self.dot.node(str(estado))
					self.caracterAnt = i
					self.estadoAnterior =  estado
					estado = 1
				elif i == 'v': #variables o puede ser una letra normal
					print(str(estado)+"->"+i)
					self.dot.node(str(estado))
					self.caracterAnt = i
					self.estadoAnterior =  estado
					estado = 2
				elif i == 'i': #sentencia if o puede ser una letra normal
					#print(str(estado)+"->"+i)
					self.dot.node(str(estado))
					self.caracterAnt = i
					self.estadoAnterior =  estado
					estado = 3
				elif i == 'f': #sentencia for o puede ser una letra normal
					print(str(estado)+"->"+i)
					self.caracterAnt = i
					self.estadoAnterior =  estado
					estado = 4
				elif i == 'w': #sentencia while o puede ser una letra normal
					print(str(estado)+"->"+i)
					self.caracterAnt = i
					self.estadoAnterior =  estado
					estado = 5
				elif i == 'd': #sentencia do o puede ser una letra normal 
					print(str(estado)+"->"+i)
					self.caracterAnt = i
					self.estadoAnterior =  estado
					estado = 6
				elif i == 'c': #sentencia continue, class, constructor o letra normal. 
					print(str(estado)+"->"+i)
					self.caracterAnt = i
					self.estadoAnterior =  estado
					estado = 7
				elif i == 'b': #sentencia break o letra normal. 
					print(str(estado)+"->"+i)
					self.caracterAnt = i
					self.estadoAnterior =  estado
					estado = 8
				elif i == 'r': #sentencia return o letra normal. 
					print(str(estado)+"->"+i)
					self.caracterAnt = i
					self.estadoAnterior =  estado
					estado = 9
			elif estado == 1: 
				if i == '*': #es comentario múltiple
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 21 #estado de letras combinadas
				elif i == '/': #es un comentario unilinea o una ruta para el destino  de los outputs
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 30 #estado de letras combinadas
			elif estado == 2:
				if i == 'a': # puede ser 'var', 'class'
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 12
				elif i == 'e': #es 'while'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 22 
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 3: 
				if i == 'f': # es if
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 23
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 4:
				if i == 'o': #puede ser 'for'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 13
				if i == 'u': #puede ser function
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 15
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 5:
				if i == 'h': #puede ser 'while
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 14
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 6:
				if i == 'o': # es do
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 24
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 7:
				if i == 'o': #puede ser 'continue' o 'constructor' o 'function'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 15
				elif i == 'l': #puede ser 'class' o 'while'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 2
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 8:
				if i == 'r': #puede ser 'break'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 9
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 9: 
				if i == 'e': #puede ser 'return' o 'break'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 16
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 10:
				if i == 'u': #puede ser function o 'return' o 'continue' o 'constructor'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 17 
				elif i == 'o': #pude ser 'constructor'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 12
				elif i == 'i': #puede ser 'function'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 14
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 11:
				if i == 'c': #sentencia continue, class, constructor o letra normal. 
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior =  estado
					estado = 7
				elif i == 'b': #sentencia break o letra normal. 
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior =  estado
					estado = 8
				elif i == 'r': #sentencia return o letra normal. 
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior =  estado
					estado = 9
				elif i == '=': 
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 34
				elif i != ' ' or i != '\n':
					#print(str(self.estadoAnterior)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 # se queda en el mismo estado
				else:
					#print(str(estado)+"->"+i+" anterior "+self.caracterAnt)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior =  estado
					estado = 11
			elif estado == 12:
				if i == 's':# puede ser 'class'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 18
				elif i == 'r':# puede ser 'var' o 'constructor'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 25
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 13:
				if i == 'r': #es 'for'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 27
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 14:
				if i == 'i': #puede ser 'while' o 'continue' o 'function'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 38
				elif i == 'o': #puede ser function
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 15
				elif i == 'r': #puede ser 'constructor'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 10
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 15:
				if i == 'n': #puede ser 'continue' o 'constructor' o 'return' o 'function'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 19
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 16:
				if i == 't':#puede ser 'return' o 'constructor' o function
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 10
				elif i == 'a': #puede ser 'break'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 20
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 17:
				if i == 'n':#puede ser function
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 17
				elif i == 'r':#puede ser 'return' 
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 15
				elif i == 'e': #puede ser 'continue'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 26
				elif i == 'c': #puede ser 'constructor' o 'function'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					self.caracterAnt = i
					self.estadoAnterior = estado
					estado = 16
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 18:
				if i == 's': # es class 
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 28
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 19: 
				if i == 't': #puede ser 'continue' o 'constructor' o 'function'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 14
				elif i == 's': #puede ser 'constructor'
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 19
				elif i == 'c': #puede ser function
					estado = 19
				elif i == ' ' or i == '\n' or i == ';' : #estado de aceptación para 'return' 
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
					#print(str(estado)+"->"+i)
					estado = 0
				else:
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 20:
				if i == 'k': #es 'break'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 29
				else:
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11 #estado de letras combinadas
			elif estado == 21:
				if i == '*': #termino comentarios multilinea
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 31
				else:
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 21
			elif estado == 22:
				if i == ' ' or i == '(': #sí es espacio se acepta la palabra reservada while.
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 36
				else:
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11
			elif estado == 23:
				if i == ' ' or i == '(': #sí es espacio se acepta la palabra reservada if.
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
					#self.estadoAnterior = estado
					estado = 36
				else:
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11
			elif estado == 24:
				if i == ' ' or i == '{': #sí es espacio se acepta la palabra reservada do.
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado					
					#print(str(estado)+"->"+i)
				estado = 11
			elif estado == 25:
				if i == ' ' or i == '(': #sí es espacio se acepta la palabra reservada var o constructor
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
				estado = 11
			elif estado == 26:
				if i == ' ' or i == ';': #sí es espacio se acepta la palabra reservada continue
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 0
				else:
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11
			elif estado == 27:
				if i == ' ' or i == '(': #sí es espacio se acepta la palabra reservada for.
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 36
				else:
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11
			elif estado == 28:
				if i == ' ': #sí es espacio se acepta la palabra reservada class.
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 0
				else:
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11
			elif estado == 29:
				if i == ' ' or i == '\n' or i == ';': #sí es espacio se acepta la palabra reservada class.
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 0
				else:
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11
			elif estado == 30:
				if i != '\n': #estado de aceptación de los comentarios unilinea
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					#print(str(estado)+"->"+i)
					estado = 30
				else:
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = 'salto'
					#self.estadoAnterior = estado
					estado = 33
			elif estado == 31:
				if i == '/':
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					#print(str(estado)+"->"+i)
					estado = 32 
				else:
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					self.caracterAnt = i
					self.estadoAnterior = estado
					estado = 0
			elif estado == 32: #estado de aceptación de comentarios multilinea
				self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
				estado = 0
			elif estado == 33: #estado de aceptación de comentarios simples
				self.generarDot(self.estadoAnterior, estado,self.caracterAnt,True,i)
				estado = 0
			elif estado == 34: #estado obtiene las asignaciones de una declaracion es de aceptación.
				if i == ';': 
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					self.generarDot(self.estadoAnterior, 35,i,True,i) #se utilizó un estado nuevo 35
					estado = 0
				elif i == '\n':
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					self.generarDot(self.estadoAnterior, 35,"salto",True,i) #se utilizó un estado nuevo 35
					estado = 0
				else:
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 34
			elif estado == 36:
				if i == 'c': #sentencia continue, class, constructor o letra normal. ****
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#print(str(estado)+"->"+i)
					#self.caracterAnt = i
					#self.estadoAnterior =  estado
					estado = 7
				elif i != '}': #cierre del if, for
					self.caracterAnt = i
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.estadoAnterior = estado
					estado = 36
				else:
					self.generarDot(self.estadoAnterior, estado,i,False,i)
					estado = 37 #estado de aceptación
			elif estado == 37: #estado de aceptación del conjunto if
				self.generarDot(self.estadoAnterior, estado,'salto',True,i)
				estado = 0
			elif estado == 38:
				if i == 'n': #puede ser 'continue'
					#print(str(estado)+"->"+i)
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 10
				elif i == 'o': #puede ser function
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 15
				else:
					self.generarDot(self.estadoAnterior, estado,self.caracterAnt,False,i)
					#self.caracterAnt = i
					#self.estadoAnterior = estado
					estado = 11

	def generarDot(self, estadoAnterior, estadoActual, caracterAnterior,esAceptacion, caracterActual):
		if esAceptacion:
			self.dot.attr('node', shape='doublecircle') #este es de aceptación
			self.dot.node(str(estadoActual))
			self.dot.attr('node', shape='circle') #regresarlo a normal
			self.dot.node(str(estadoAnterior))
			self.dot.edge(str(estadoAnterior), str(estadoActual), label = caracterAnterior)
		else:
			self.dot.node(str(estadoActual))
			self.dot.node(str(estadoAnterior))
			self.dot.edge(str(estadoAnterior), str(estadoActual), label = caracterAnterior)
		if caracterActual == '\n':
			caracterActual = 'salto'
		self.caracterAnt = caracterActual
		self.estadoAnterior= estadoActual

