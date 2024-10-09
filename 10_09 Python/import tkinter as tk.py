import tkinter as tk
#
# FUNCIONS EVENTS
# RELACIONATS AMB ELS WIDGETS
#

def llegirentry():
    pass

#root
root = tk.Tk()
amplada = root.winfo_screenwidth()
alcada = root.winfo_screenheight()
strink = '{}x{}'.format(amplada , alcada)
root.geometry(strink)
root.attributes('-fullscreen', True)

#canvas
c = tk.Canvas(root, bg ='orange')
c.place(x = 0, y = 0, width = amplada, height = alcada) # division entera para cambiar tamaños//

#boto
boto  = tk.Button(c, text = "Hazme Click",command=llegirentry)
boto.place(x = amplada //2, y = (9*alcada) // 10, width=100, height=25,anchor=tk.CENTER)

#entrada
Entrada = tk.Entry()
Entrada.place(x = amplada //2, y = (7*alcada) // 10, width=100, height=25,anchor=tk.CENTER)#Tk.CENTER CENTRA

labeltext1 = tk.Label(c, text = "Resultat", bg=c.cget('bg'))
labeltext1.place(x = amplada //2, y = (4*alcada) // 10, width=100, height=25,anchor=tk.CENTER)

#volem q al entrar unes dades a entry i donem boto pinti les dades.

#
# ESPAI PER DEFINICIO DE WIDGETS
# CRIDA A FUNCIONS DE CADA WIDGET I EVENTS
# LÒGICA DEL PROGRAMA
# CRIDA A ALTRES FUNCIONS DE LA LÒGICA DEL PROGRAMA
#

root.mainloop()

