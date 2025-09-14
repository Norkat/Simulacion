from tkinter import *
from tkinter import messagebox

# Crear la ventana principal
raiz = Tk()
raiz.title("Calcula el RFC")

# Crear un frame dentro de la ventana principal
MiFrame = Frame(raiz, width=900, height=600)
MiFrame.pack(side="left", anchor="n")

# Crear los widgets de entrada
Cuadronombre = Entry(MiFrame)
Cuadronombre.grid(row=0, column=1, padx=10, pady=10)
NombreLabel = Label(MiFrame, text="Nombre:")
NombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

Cuadroapellido = Entry(MiFrame)
Cuadroapellido.grid(row=1, column=1, padx=10, pady=10)
apellido1Label = Label(MiFrame, text="Primer Apellido:")
apellido1Label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

Cuadroapellido2 = Entry(MiFrame)
Cuadroapellido2.grid(row=2, column=1, padx=10, pady=10)
apellido2Label = Label(MiFrame, text="Segundo Apellido:")
apellido2Label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

CuadroDia = Entry(MiFrame)
CuadroDia.grid(row=1, column=2, padx=10, pady=10)
DiaLabel = Label(MiFrame, text="Día:")
DiaLabel.grid(row=0, column=2, sticky="e", padx=10, pady=10)

CuadroMes = Entry(MiFrame)
CuadroMes.grid(row=1, column=3, padx=10, pady=10)
MesLabel = Label(MiFrame, text="Mes:")
MesLabel.grid(row=0, column=3, sticky="e", padx=10, pady=10)

CuadroAño = Entry(MiFrame)
CuadroAño.grid(row=1, column=4, padx=10, pady=10)
AñoLabel = Label(MiFrame, text="Año:")
AñoLabel.config(justify="left")
AñoLabel.grid(row=0, column=4, sticky="e", padx=10, pady=10)

# Crear el Text widget para mostrar el RFC y deshabilitarlo para que no sea editable
Cuadrorfc = Text(MiFrame, height=1, width=20)
Cuadrorfc.grid(row=3, column=1, padx=10, pady=10)
Cuadrorfc.config(state=DISABLED)
rfcLabel = Label(MiFrame, text="RFC:")
rfcLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

def RFC():
    primerdigito = Cuadronombre.get()
    apellidopa = Cuadroapellido.get()
    apellidoma = Cuadroapellido2.get()
    dia = CuadroDia.get().zfill(2)  # Asegura que el día tenga 2 dígitos
    mes = CuadroMes.get().zfill(2)  # Asegura que el mes tenga 2 dígitos
    año = CuadroAño.get()[-2:]  # Toma los últimos 2 dígitos del año
    
    primerLetra = apellidopa[0].upper()
    vocales = 'AEIOU'
    vocalInterna = ''
    for letra in apellidopa[1:].upper():
        if letra in vocales:
            vocalInterna = letra
            break
    primerMat = apellidoma[0].upper() if apellidoma else ''
    primerNom = primerdigito[0].upper() if primerdigito else ''
    
    rfc = primerLetra + vocalInterna + primerMat + primerNom + año + mes + dia
    
    # Habilita el Text widget, inserta el RFC, y lo deshabilita nuevamente
    Cuadrorfc.config(state=NORMAL)
    Cuadrorfc.delete("1.0", END)  # Borra cualquier texto anterior
    Cuadrorfc.insert(END, rfc)
    Cuadrorfc.config(state=DISABLED)

# Crear el botón para calcular el RFC
Botonrfc = Button(MiFrame, text="Calcula el RFC", command=RFC)
Botonrfc.grid(row=2, column=3, sticky="e", padx=10, pady=10)

# Ejecutar el bucle principal de la ventana
raiz.mainloop()