from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import random as r


def limpiarFrame(frame):
    for widgets in frame.winfo_children():
        widgets.pack_forget()


def comprobarEntry():
    dato = entryManual.get()
    if dato == "" or not dato.isdecimal() or int(dato) < 1:
        messagebox.showwarning("Advertencia", "Datos Invalidos")
    else:
        florista(int(dato))


def florista(numFlores):

    limpiarFrame(window)

    frameFlorista = Frame(window, width=640, height=360)
    frameFlorista.config(background='pink')
    frameFlorista.pack(fill='both', expand=True)

    datosTabla = []
    utilidadAnual = 0

    for i in range(1, 366):
        numero = round(r.random(), 4)
        demanda = ""
        if numero <= 0.07:
            demanda = 6
        elif numero <= 0.22:
            demanda = 12
        elif numero <= 0.32:
            demanda = 24
        elif numero <= 0.57:
            demanda = 36
        elif numero <= 0.77:
            demanda = 48
        elif numero <= 0.82:
            demanda = 60
        elif numero <= 0.9:
            demanda = 100
        elif numero <= 0.96:
            demanda = 200
        elif numero <= 1:
            demanda = 500
        floresVendidas = 0
        floresNoVendidas = 0

        if demanda >= numFlores:
            floresVendidas = numFlores
            floresNoVendidas = 0
        else:
            floresVendidas = demanda
            floresNoVendidas = numFlores - demanda

        costoCompra = 100 * numFlores
        ingVentas = 160 * floresVendidas
        ingDiaSig = 50 * floresNoVendidas
        utilidadDiaria = (ingVentas+ingDiaSig) - costoCompra
        utilidadAnual += utilidadDiaria

        datosTabla.append([i, numero, demanda, numFlores, floresVendidas, floresNoVendidas,
                          costoCompra, ingVentas, ingDiaSig, utilidadDiaria])

    tabla = ttk.Treeview(frameFlorista, columns=(
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10), show='headings', height=20)
    tabla.pack(side=LEFT, fill=BOTH, expand=True)

    tabla.column("#1", anchor="center", width=50)
    tabla.column("#2", anchor="center", width=100)
    tabla.column("#3", anchor="center", width=100)
    tabla.column("#4", anchor="center", width=100)
    tabla.column("#5", anchor="center", width=100)
    tabla.column("#6", anchor="center", width=100)
    tabla.column("#7", anchor="center", width=150)
    tabla.column("#8", anchor="center", width=100)
    tabla.column("#9", anchor="center", width=100)
    tabla.column("#10", anchor="center", width=100)

    tabla.heading(1, text="Dia")
    tabla.heading(2, text="#Aleatorio")
    tabla.heading(3, text="Demanda por dia")
    tabla.heading(4, text="Flores(compra)")
    tabla.heading(5, text="Vendidas")
    tabla.heading(6, text="No Vendidas")
    tabla.heading(7, text="Costo")
    tabla.heading(8, text="Ing.Venta")
    tabla.heading(9, text="Ing.Venta Dia Siguiente")
    tabla.heading(10, text="Utilidad")

    for dato in datosTabla:
        tabla.insert("", "end", values=dato)

    # Creamos un scrollbar para la tabla
    scrollbar_tabla = ttk.Scrollbar(
        frameFlorista, orient=VERTICAL, command=tabla.yview)
    scrollbar_tabla.pack(side=RIGHT, fill=Y)
    tabla.configure(yscrollcommand=scrollbar_tabla.set)

    print(utilidadAnual/365)


# Ventana principal
window = Tk()
window.geometry('640x360')
window.resizable(True, True)
window.title('')

frameSeleccion = Frame(window, width=640, height=360)
frameSeleccion.config(background='cyan')
frameSeleccion.pack(fill='both', expand=True)

labelTitulo = Label(
    frameSeleccion, text='Examen Unidad 2 - Rafael Payan', font=('KacstDecorative', 10, ))
labelTitulo.config(bg='cyan')
labelTitulo.pack(padx=5, pady=5)

labelCantFlo = Label(
    frameSeleccion, text='¿Cuántas flores desea comprar?', font=('KacstDecorative', 20, ))
labelCantFlo.config(bg='cyan')
labelCantFlo.pack(padx=5, pady=5)

entryManual = Entry(frameSeleccion, font=25, width=25)
entryManual.pack(padx=5, pady=5)

botonEnviar = Button(frameSeleccion, text='Enviar', command=comprobarEntry)
botonEnviar.config(font=15, width=20, height=2)
botonEnviar.pack(pady=10)

botonSalir = Button(
    frameSeleccion, text='Salir', command=window.quit,)
botonSalir.config(font=10, width=20, height=2)
botonSalir.pack(pady=10)

window.mainloop()
