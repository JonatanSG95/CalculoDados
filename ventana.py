from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dados import dados_base

ventana_principal = Tk()
ventana_principal.title("Calculadora")
ventana_principal.minsize(width=800, height=600)
ventana_principal.config(padx= 25, pady=25)


mensaje = Label(ventana_principal, text='Elija que dado tirar')

mensaje.pack()

def mostrar_seleccionado():
    elegido = lista.get()
    messagebox.showinfo(
        message=f"La opcion seleccionada es: {elegido}",
        title="seleccion"
    )

lista = ttk.Combobox(
    state="readonly",
    values=dados_base
)
lista.set(dados_base[0])
lista.place(x=50, y=50)

boton = ttk.Button(text="Elegir", command=mostrar_seleccionado)
boton.place(x=50,y=100)

ventana_principal.mainloop()