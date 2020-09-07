from tkinter import *
from tkinter import filedialog, ttk
import tkinter as tk
import analisisJS as js
import os
import re

class App():
    def __init__(self):

        title = 'WEB EDITOR'
        self.root = Tk()
        self.root.geometry('1000x600')
        #self.root.iconbitmap('icon.ico')
        self.root.title(title)

        bottomFrame = Frame(self.root, width=600, height=100)
        bottomFrame.pack(side = BOTTOM)
        consola = Text(bottomFrame,width=600, height=10, bg='#000000', foreground = '#ffffff')
        consola.pack(side = BOTTOM)
        #consola.insert(INSERT,">")

        self.tabs = {'ky': 0}
        #Keep a record of the open tabs in a list.
        self.tab_list = []
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand = True, fill= 'both')

        #variable que obtiene el texto
        self.texto_obtenido = ""
        #variable que hace el análisis de la ejecución
        self.ejecutar = None
        #variable que obtiene el path absoluto del archivo
        self.path = None

        menubar = Menu(self.root)
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nueva pestaña", command=self.generate_tab)
        filemenu.add_command(label="Abrir", command = self.open_file)
        filemenu.add_command(label="Guardar", command= self.save_file)
        filemenu.add_command(label="Guardar Como", command= self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command= self.root.quit)
        menubar.add_cascade(label="Archivo", menu = filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Ejecutar análisis", command = self.analisis)
        editmenu.add_separator()
        menubar.add_cascade(label="Análisis", menu=editmenu)
        editReportes = Menu(menubar, tearoff=0)
        editReportes.add_command(label="Árbol generado JS")
        editReportes.add_command(label="Bitácora recorrido CSS")
        editReportes.add_command(label="Reporte errores léxicos")
        editReportes.add_command(label="Reporte de análisis sintáctico")
        editReportes.add_separator()
        menubar.add_cascade(label="Reportes", menu=editReportes)
        self.root.config(menu=menubar)

    #función que inicia el análisis del código
    def analisis(self):
        valor = self.ejecutar
        #if valor != None and self.texto_obtenido != None :
            #self.texto_obtenido.delete(1.0, "end-1c") 
            #print("estoy en el análisis" + valor)
        if self.texto_obtenido != None:
            valor = self.texto_obtenido.get("1.0", "end-1c")
            self.texto_obtenido = None
            #print(valor)
        self.ejecutar = None
         #split por punto y se obtiene la extensión del archivo.
        splitear = self.path.split('.')
        if splitear[1] == 'js':
            analisis1 = js.JS(valor)
            analisis1.ejecucion()
            analisis1.ejecutarDot()
            print('es archivo js')
        elif splitear[1] == 'css':
            print('es archivo css')
        elif splitear[1] == 'html':
            print('es archivo html')

    def open_file(self):
        file = open(filedialog.askopenfilename(), 'r+')
        text_value = file.read()
        #print(text_value) #obtener texto aquí.
        self.texto_obtenido.delete(1.0, "end-1c") 
        self.texto_obtenido.insert("end-1c", text_value) #carga texto en el tab
        self.ejecutar = text_value
        #self.cambiarColores(self.texto_obtenido, text_value) #cambiar colores
        #title = os.path.basename(file.name)
        print("ruta absoluta del archivo" + os.path.abspath(file.name))
        self.path = os.path.abspath(file.name)
        file.close()

    #funcion para cambiar colores
    def cambiarColores(self, txt, texto):
        txt.delete(1.0, "end-1c") 
        txt.tag_config('reservadas', foreground="red")
        txt.tag_config('intBoolean', foreground="black")

        nuevo = re.sub(r'\n|\t|\r', ' ', texto)
        match = nuevo.split(' ')
        cont = 0
        for i in match:
	        if i == "hola":
		        txt.high('end', i, 'reservadas')
		        txt.insert('end', ' ' )
	        else:
		        txt.insert('end', i, 'intBoolean')
		        txt.insert('end', ' ' )

    def add_tab(self, name):
        tab = Tab(self.notebook, name)
        print(name)
        self.notebook.add(tab, text=name)
        self.tab_list.append(tab)
        self.texto_obtenido = tab.getTexto(); #se obtiene el textwidget
        #tab.setTexto(tab.getTexto())

    def save_file(self):
        tab_to_save = self.get_tab()
        print(tab_to_save)
        tab_to_save.save_tab()

    def get_tab(self):
        print(self.notebook.index('current'))
        #Get the tab object from the tab_list based on the index of the currently selected tab
        tab = self.tab_list[self.notebook.index('current')]
        return tab

    def generate_tab(self):
        if self.tabs['ky'] < 20:
            self.tabs['ky'] += 1
            self.add_tab('Archivo ' + str(self.tabs['ky']))

    def run(self):
        self.root.mainloop()

class TextLineNumbers(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def getTexto(self):
        return self.textwidget;

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")
        
        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

class CustomText(Text):
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)
        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or 
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result  


class Tab(Frame):

    def __init__(self, root, name):
        Frame.__init__(self, root)

        self.root = root
        self.name = name

        self.textWidget = Text(self)
        #self.textWidget.pack(expand=True, fill='both')
        self.text = CustomText(self)
        self.vsb = Scrollbar(orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)
        

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.linenumbers.redraw()

    def save_tab(self):
        print(self.textWidget.get("1.0", 'end-1c'))
        file = open(filedialog.asksaveasfilename() + '.txt', 'w+')
        file.write(self.textWidget.get("1.0", 'end-1c'))
        print(os.path.basename(file.name))
        #title = os.path.basename(file.name)
        file.close()

    def getTexto(self):
        return self.linenumbers.getTexto()



if __name__ == '__main__':
    app1 = App()
    app1.run()
