import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class ProyectosMarval:

    @staticmethod
    def proyecto_marval():
        try:
            base = tk.Tk()  # Crear ventana principal
            base.geometry("1200x400")
            base.title("Gestión de Proyectos - Marval")

            groupBox = LabelFrame(base,text="Datos de los Proyectos",padx=5,pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelNombre_del_Proyecto=Label(groupBox,text="Id Proyecto:",width=13,font=("arial",12)).grid(row=0,column=0)
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=0,column=1)

            labelCiudad_del_Proyecto=Label(groupBox,text="Nombre:",width=13,font=("arial",12)).grid(row=1,column=0)
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=1,column=1)

            labelBarrio_del_Proyecto=Label(groupBox,text="Ciudad:",width=13,font=("arial",12)).grid(row=2,column=0)
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=2,column=1)
            
            labelEstado_del_Proyecto=Label(groupBox,text="estado:",width=13,font=("arial",12)).grid(row=3,column=0)
            seleccionEstado = tk.StringVar()
            combo = ttk.Combobox(groupBox,values=["En constrccion","Terminado"],textvariable=seleccionEstado)
            combo.grid(row=3,column=1)
            seleccionEstado.set("Terminado")
            
            Button(groupBox,text="Guardar",width=10).grid(row=4,column=0)
            Button(groupBox,text="Modificar",width=10).grid(row=4,column=1)
            Button(groupBox,text="Eliminar",width=10).grid(row=4,column=2)
            
            groupBox = LabelFrame(base,text="Lista del Proyecto",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            
            tree = ttk.Treeview(groupBox,columns=("Id Proyecto","Ciudad","Barrio","Estado"),show='headings')
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1",text="Id del Proyecto")
            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2",text="Nombre")
            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3",text="Ciudad")
            tree.column("# 4",anchor=CENTER)
            tree.heading("# 4",text="Estado")
            
            tree.pack()




            base.mainloop()  # Mantener la ventana abierta

            
        except Exception as error:
            print("Error al mostrar la interfaz, error: {}".format(error))

# Llamar al método
ProyectosMarval.proyecto_marval()

