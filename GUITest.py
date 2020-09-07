pr = '//PATHW:E:// \n\n' #path
splitear = pr.split('//PATHW:')
splitear1 = splitear[1].split('\n')
print(splitear1[0])

"""from graphviz import Digraph



dot = Digraph(format='png')
dot.node('0', 'i')
dot.node('1', 'j');
dot.edge('0','1')
dot.edge('1','0')
dot.render('.\\tabla.dot', view=True)"""

"""import tkinter as tk
import re

root = tk.Tk()

txt = tk.Text(root)
txt.pack()

txt.tag_config('warning', foreground="red")
txt.tag_config('reser', foreground="blue")

texto = "hola mundo hola\n hola hola \tagh"
nuevo = re.sub(r'\n|\t|\r', ' ', texto)

match = nuevo.split(' ')
cont = 0
for i in match:
	if i == "hola":
		txt.insert('end', i, 'warning')
		txt.insert('end', ' ' )
	else:
		txt.insert('end', i)
		txt.insert('end', ' ' )

	if(cont == 3):
		txt.insert('end', '\n')
	cont = cont+1
"""

#txt.insert('end', "Hello\n")
#txt.insert('end', "Alert #1\n", 'warning')
#txt.insert('end', "World\n")
#txt.insert('end', "Alert #2\n", 'warning')
#txt.insert('end', "hola", 'reser')

#root.mainloop()