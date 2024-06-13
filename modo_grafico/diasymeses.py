from tkinter import *
from tkinter import ttk

def agrega():
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes",
        "Sabado", "Domingo")
    encontrado = False
    for mimes in meses:
        if mimes.upper() == vartexto.get().upper():
            textomes.set(textomes.get() + "\n" + mimes)
            vartexto.set("")
            encontrado = True
    if not encontrado:
        for midia in dias:
            if midia.upper() == vartexto.get().upper():
                textodia.set(textodia.get() + "\n" + midia)
                vartexto.set("")
                encontrado = True
    textoerror.set("")
    if not encontrado:
        textoerror.set("Palabra no reconocida")


ventana = Tk()
ventana.title("Días y Meses")
ventana.geometry("400x300")
ventana.resizable(False, True)
ventana.minsize(400, 200)
ventana.maxsize(400, 500)

ttk.Style().configure("Cyan.TFrame", background="cyan")
zona1 = ttk.Frame(ventana, width=150, height=10, style="Cyan.TFrame")
zona1.pack(side=TOP, expand=True, fill=BOTH)

textoerror = StringVar()
ttk.Style().configure("Cyan.TLabel", background="cyan")
ttk.Label(zona1, textvariable=textoerror, style="Cyan.TLabel").pack(side=BOTTOM)

ttk.Style().configure("Yellow.TLabel", background="yellow")
ttk.Label(zona1, text="Escriba el nombre:", style="Yellow.TLabel").pack(side=LEFT)  # Se alineará en la parte izquierda
vartexto = StringVar()
cuadro = ttk.Entry(zona1, textvariable=vartexto, width=15)
cuadro.pack(side=LEFT)  # Se alineará a continuación de la etiqueta
ttk.Style().configure("Green.TButton", background="green")
ttk.Button(zona1, text="Introducir", style="Green.TButton", command=agrega).pack(side=RIGHT)  # Se alineará a la derecha

ttk.Style().configure("Gray.TFrame", background="gray")
zona2 = ttk.Frame(ventana, width=30, height=30, style="Gray.TFrame")
zona2.pack(side=BOTTOM, expand=True, fill=X)
textodia = StringVar()
textodia.set("DIAS:")
ttk.Label(zona2, text="DÍAS:", textvariable=textodia, style="Yellow.TLabel").pack(side=LEFT)
textomes = StringVar()
textomes.set("MESES:")
ttk.Label(zona2, textvariable=textomes, style="Cyan.TLabel").pack(side=RIGHT)

ventana.mainloop()
