import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from proyectos import *
from connection import *


class ProyectosMarval:

    global base
    base = None

    global texBoxId
    texBoxId = None

    global texBoxNombre
    texBoxNombre = None

    global texBoxCiudad
    texBoxCiudad = None

    global combo
    combo = None

    global groupBox
    groupBox = None

    global tree
    tree = None

    @staticmethod
    def proyecto_marval():

        global base
        global texBoxId
        global texBoxNombre
        global texBoxCiudad
        global combo
        global groupBox
        global tree

        try:
            base = tk.Tk()
            base.geometry("1200x400")
            base.title("Gestión de Proyectos - Marval")

            groupBox = LabelFrame(base, text="Datos de los Proyectos", padx=5, pady=5)
            groupBox.grid(row=0, column=0, padx=10, pady=10)

            Label(groupBox, text="Id Proyecto:", width=13, font=("arial", 12)).grid(row=0, column=0)
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=0, column=1)

            Label(groupBox, text="Nombre:", width=13, font=("arial", 12)).grid(row=1, column=0)
            texBoxNombre = Entry(groupBox)
            texBoxNombre.grid(row=1, column=1)

            Label(groupBox, text="Ciudad:", width=13, font=("arial", 12)).grid(row=2, column=0)
            texBoxCiudad = Entry(groupBox)
            texBoxCiudad.grid(row=2, column=1)

            Label(groupBox, text="Estado:", width=13, font=("arial", 12)).grid(row=3, column=0)
            seleccionEstado = tk.StringVar()
            combo = ttk.Combobox(
                groupBox,
                values=["En construccion", "Terminado"],
                textvariable=seleccionEstado
            )
            combo.grid(row=3, column=1)
            seleccionEstado.set("Terminado")

            Button(groupBox, text="Guardar", width=10, command=guardar_registro).grid(row=4, column=0)
            Button(groupBox, text="Modificar", width=10, command=modificar_registro).grid(row=4, column=1)
            Button(groupBox, text="Eliminar", width=10,command =eliminar_registro).grid(row=4, column=2)

            groupBox = LabelFrame(base, text="Lista del Proyecto", padx=5, pady=5)
            groupBox.grid(row=0, column=1, padx=5, pady=5)

            tree = ttk.Treeview(
                groupBox,
                columns=("Id Proyecto", "Nombre", "Ciudad", "Estado"),
                show='headings'
            )

            tree.column("#1", anchor=CENTER)
            tree.heading("#1", text="Id del Proyecto")
            tree.column("#2", anchor=CENTER)
            tree.heading("#2", text="Nombre")
            tree.column("#3", anchor=CENTER)
            tree.heading("#3", text="Ciudad")
            tree.column("#4", anchor=CENTER)
            tree.heading("#4", text="Estado")



            for row in proyectos.mostar_proyectos():
                tree.insert("","end",values=row)


            tree.bind("<<TreeviewSelect>>",seleccionar_registro)


            tree.pack()

            base.mainloop()

        except Exception as error:
            print(f"Error al mostrar la interfaz: {error}")


def guardar_registro():

    global texBoxNombre
    global texBoxCiudad
    global combo

    try:
        if texBoxNombre is None or texBoxCiudad is None or combo is None:
            print("Los elementos de la interfaz no están inicializados")
            return

        nombre = texBoxNombre.get()
        ciudad = texBoxCiudad.get()
        estado = combo.get()

        proyectos.ingresar_proyectos(nombre, ciudad, estado)

        messagebox.showinfo("Información", "Los datos fueron guardados")

        actualizar_treeview()

        texBoxNombre.delete(0, END)
        texBoxCiudad.delete(0, END)

    except ValueError as error:
        print(f"Error al ingresar los datos: {error}")

def actualizar_treeview():
    global tree

    try:
        tree.delete(*tree.get_children())

        datos = proyectos.mostar_proyectos()

        for row in proyectos.mostar_proyectos():
                tree.insert("","end",values=row)

    except ValueError as error:
        print("Error al actualizar tabla{}".format(error))



def seleccionar_registro(event):
    try:
        item_seleccionado = tree.focus()

        if item_seleccionado:
            values = tree.item(item_seleccionado)['values']

            texBoxId.delete(0,END)
            texBoxId.insert(0,values[0])
            texBoxNombre.delete(0,END)
            texBoxNombre.insert(0,values[1])
            texBoxCiudad.delete(0,END)
            texBoxCiudad.insert(0,values[2])
            combo.set(values[3])

    except ValueError as error:
        print("Error al seleccionar registro{}".format(error))



def modificar_registro():

    global texBoxNombre
    global texBoxCiudad
    global combo
    global texBoxId
    global groupBox

    try:
        if texBoxId is None or texBoxNombre is None or texBoxCiudad is None or combo is None:
            print("Los elementos de la interfaz no están inicializados")
            return
        
        idproyecto = texBoxId.get()
        nombre = texBoxNombre.get()
        ciudad = texBoxCiudad.get()
        estado = combo.get()

        proyectos.modificar_proyectos(idproyecto,nombre, ciudad, estado)

        messagebox.showinfo("Información", "Los datos fueron actualizados")

        actualizar_treeview()
        texBoxId.delete(0, END)
        texBoxNombre.delete(0, END)
        texBoxCiudad.delete(0, END)

    except ValueError as error:
        print(f"Error al modificar los datos: {error}")


def eliminar_registro():

    global texBoxId
    global texBoxNombre
    global texBoxCiudad
    

    try:
        if texBoxId is None :
            print("Los elementos de la interfaz no están inicializados")
            return
        
        idproyecto = texBoxId.get()
        

        proyectos.eliminar_proyectos(idproyecto)

        messagebox.showinfo("Información", "Los datos fueron eliminados")

        actualizar_treeview()
        texBoxId.delete(0, END)
        texBoxNombre.delete(0, END)
        texBoxCiudad.delete(0, END)

    except ValueError as error:
        print(f"Error al modificar los datos: {error}")
# Llamar al método
ProyectosMarval.proyecto_marval()


