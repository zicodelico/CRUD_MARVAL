import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from proyectos import *
from connection import *


class ProyectosMarval:

    global base, texBoxId, texBoxNombre, texBoxCiudad, combo, tree
    base = texBoxId = texBoxNombre = texBoxCiudad = combo = tree = None

    @staticmethod
    def proyecto_marval():

        global base, texBoxId, texBoxNombre, texBoxCiudad, combo, tree

        try:
            base = tk.Tk()
            base.geometry("1350x560")
            base.title("Gestión de Proyectos - Marval")
            base.configure(bg="#eef1f4")

            # ================= PANEL IZQUIERDO =================
            panel_form = Frame(base, bg="#ffffff", bd=1, relief=SOLID)
            panel_form.grid(row=0, column=0, padx=20, pady=20, sticky="n")

            Label(panel_form, text="Datos del Proyecto",
                  bg="#ffffff", font=("Segoe UI", 13, "bold")
                  ).grid(row=0, column=0, columnspan=2, pady=(15, 20))

            Label(panel_form, text="ID Proyecto", bg="#ffffff").grid(row=1, column=0, sticky="w", padx=20)
            texBoxId = Entry(panel_form, width=30)
            texBoxId.grid(row=1, column=1, pady=5, padx=20)

            Label(panel_form, text="Nombre", bg="#ffffff").grid(row=2, column=0, sticky="w", padx=20)
            texBoxNombre = Entry(panel_form, width=30)
            texBoxNombre.grid(row=2, column=1, pady=5, padx=20)

            Label(panel_form, text="Ciudad", bg="#ffffff").grid(row=3, column=0, sticky="w", padx=20)
            texBoxCiudad = Entry(panel_form, width=30)
            texBoxCiudad.grid(row=3, column=1, pady=5, padx=20)

            Label(panel_form, text="Estado", bg="#ffffff").grid(row=4, column=0, sticky="w", padx=20)
            seleccionEstado = tk.StringVar()
            combo = ttk.Combobox(
                panel_form,
                values=["En construccion", "Sobre planos", "Terminado"],
                textvariable=seleccionEstado,
                state="readonly",
                width=28
            )
            combo.grid(row=4, column=1, pady=5, padx=20)
            seleccionEstado.set("Terminado")

            barra = Frame(panel_form, bg="#ffffff")
            barra.grid(row=5, column=0, columnspan=2, pady=25)

            Button(barra, text="Guardar", width=11, bg="#2e7d32", fg="white",
                   command=guardar_registro).grid(row=0, column=0, padx=6)
            Button(barra, text="Modificar", width=11, bg="#1565c0", fg="white",
                   command=modificar_registro).grid(row=0, column=1, padx=6)
            Button(barra, text="Eliminar", width=11, bg="#c62828", fg="white",
                   command=eliminar_registro).grid(row=0, column=2, padx=6)

            # ================= PANEL DERECHO =================
            panel_lista = Frame(base, bg="#ffffff", bd=1, relief=SOLID)
            panel_lista.grid(row=0, column=1, padx=10, pady=20, sticky="n")

            Label(panel_lista, text="Listado de Proyectos",
                  bg="#f5f7fa", font=("Segoe UI", 13, "bold"),
                  anchor="w", padx=15, pady=8).pack(fill=X)

            tabla_frame = Frame(panel_lista, bg="#ffffff", bd=1, relief=SOLID)
            tabla_frame.pack(padx=10, pady=5)

            style = ttk.Style()
            style.configure("Treeview",
                            font=("Segoe UI", 9),
                            rowheight=26,
                            borderwidth=1,
                            relief="solid",
                            background="#ffffff",
                            fieldbackground="#ffffff")
            style.map("Treeview",
                      background=[("selected", "#1976d2")],
                      foreground=[("selected", "white")])

            style.configure("Treeview.Heading",
                            font=("Segoe UI", 10, "bold"))

            scrollbar = Scrollbar(tabla_frame)
            scrollbar.pack(side=RIGHT, fill=Y)

            tree = ttk.Treeview(
                tabla_frame,
                columns=("Id", "Nombre", "Ciudad", "Estado"),
                show="headings",
                yscrollcommand=scrollbar.set,
                height=15
            )
            scrollbar.config(command=tree.yview)

            # ---------- ORDEN POR COLUMNA ----------
            def ordenar(col, reverse):
                data = [(tree.set(k, col), k) for k in tree.get_children("")]
                data.sort(reverse=reverse)
                for index, (_, k) in enumerate(data):
                    tree.move(k, "", index)
                tree.heading(col, command=lambda: ordenar(col, not reverse))

            for col in ("Id", "Nombre", "Ciudad", "Estado"):
                tree.heading(col, text=col, command=lambda c=col: ordenar(c, False))

            tree.column("Id", width=80, anchor=CENTER)
            tree.column("Nombre", width=240)
            tree.column("Ciudad", width=180)
            tree.column("Estado", width=140, anchor=CENTER)

            # ---------- EFECTO CUADRÍCULA ----------
            tree.tag_configure("odd", background="#f9f9f9")
            tree.tag_configure("even", background="#e9eef3")
            tree.tag_configure("hover", background="#dbe9f6")

            for index, row in enumerate(proyectos.mostar_proyectos()):
                tag = "even" if index % 2 == 0 else "odd"
                tree.insert("", END, values=row, tags=(tag,))

            # ---------- HOVER ----------
            def on_motion(event):
                row_id = tree.identify_row(event.y)
                for item in tree.get_children():
                    tree.item(item, tags=("even" if int(tree.index(item)) % 2 == 0 else "odd",))
                if row_id:
                    tree.item(row_id, tags=("hover",))

            tree.bind("<Motion>", on_motion)
            tree.bind("<<TreeviewSelect>>", seleccionar_registro)
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


