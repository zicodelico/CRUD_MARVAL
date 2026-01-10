# ===================== IMPORTACIONES =====================
# Tkinter: librería estándar de Python para interfaces gráficas
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Importación de la lógica del CRUD (modelo)
from proyectos import *

# Importación de la conexión a base de datos
from connection import *


# ===================== CLASE PRINCIPAL DE LA INTERFAZ =====================
class ProyectosMarval:

    # Variables globales para poder acceder a los widgets desde otras funciones
    global base, texBoxId, texBoxNombre, texBoxCiudad, combo, tree
    base = texBoxId = texBoxNombre = texBoxCiudad = combo = tree = None

    # Método estático que construye toda la ventana principal
    @staticmethod
    def proyecto_marval():

        # Declaración de variables globales dentro del método
        global base, texBoxId, texBoxNombre, texBoxCiudad, combo, tree

        try:
            # ----------------- VENTANA PRINCIPAL -----------------
            base = tk.Tk()  # Se crea la ventana raíz
            base.geometry("1350x560")  # Tamaño de la ventana
            base.title("Gestión de Proyectos - Marval")  # Título
            base.configure(bg="#eef1f4")  # Color de fondo

            # ================= PANEL IZQUIERDO (FORMULARIO CRUD) =================
            # Contenedor del formulario
            panel_form = Frame(base, bg="#ffffff", bd=1, relief=SOLID)
            panel_form.grid(row=0, column=0, padx=20, pady=20, sticky="n")

            # Título del formulario
            Label(
                panel_form,
                text="Datos del Proyecto",
                bg="#ffffff",
                font=("Segoe UI", 13, "bold")
            ).grid(row=0, column=0, columnspan=2, pady=(15, 20))

            # Campo ID (normalmente se usa para modificar y eliminar)
            Label(panel_form, text="ID Proyecto", bg="#ffffff").grid(row=1, column=0, sticky="w", padx=20)
            texBoxId = Entry(panel_form, width=30)
            texBoxId.grid(row=1, column=1, pady=5, padx=20)

            # Campo Nombre
            Label(panel_form, text="Nombre", bg="#ffffff").grid(row=2, column=0, sticky="w", padx=20)
            texBoxNombre = Entry(panel_form, width=30)
            texBoxNombre.grid(row=2, column=1, pady=5, padx=20)

            # Campo Ciudad
            Label(panel_form, text="Ciudad", bg="#ffffff").grid(row=3, column=0, sticky="w", padx=20)
            texBoxCiudad = Entry(panel_form, width=30)
            texBoxCiudad.grid(row=3, column=1, pady=5, padx=20)

            # Campo Estado (ComboBox)
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

            # Barra de botones CRUD
            barra = Frame(panel_form, bg="#ffffff")
            barra.grid(row=5, column=0, columnspan=2, pady=25)

            # Botón CREATE
            Button(
                barra, text="Guardar", width=11, bg="#2e7d32", fg="white",
                command=guardar_registro
            ).grid(row=0, column=0, padx=6)

            # Botón UPDATE
            Button(
                barra, text="Modificar", width=11, bg="#1565c0", fg="white",
                command=modificar_registro
            ).grid(row=0, column=1, padx=6)

            # Botón DELETE
            Button(
                barra, text="Eliminar", width=11, bg="#c62828", fg="white",
                command=eliminar_registro
            ).grid(row=0, column=2, padx=6)

            # ================= PANEL DERECHO (READ / LISTADO) =================
            panel_lista = Frame(base, bg="#ffffff", bd=1, relief=SOLID)
            panel_lista.grid(row=0, column=1, padx=10, pady=20, sticky="n")

            # Título del listado
            Label(
                panel_lista,
                text="Listado de Proyectos",
                bg="#f5f7fa",
                font=("Segoe UI", 13, "bold"),
                anchor="w",
                padx=15,
                pady=8
            ).pack(fill=X)

            # Contenedor del Treeview
            tabla_frame = Frame(panel_lista, bg="#ffffff", bd=1, relief=SOLID)
            tabla_frame.pack(padx=10, pady=5)

            # Estilos del Treeview
            style = ttk.Style()
            style.configure("Treeview",
                            font=("Segoe UI", 9),
                            rowheight=26,
                            borderwidth=1,
                            relief="solid",
                            background="#ffffff",
                            fieldbackground="#ffffff")

            # Estilo para selección
            style.map("Treeview",
                      background=[("selected", "#1976d2")],
                      foreground=[("selected", "white")])

            style.configure("Treeview.Heading",
                            font=("Segoe UI", 10, "bold"))

            # Scroll vertical
            scrollbar = Scrollbar(tabla_frame)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Treeview (tabla de datos)
            tree = ttk.Treeview(
                tabla_frame,
                columns=("Id", "Nombre", "Ciudad", "Estado"),
                show="headings",
                yscrollcommand=scrollbar.set,
                height=15
            )
            scrollbar.config(command=tree.yview)

            # ================= ORDENAMIENTO POR COLUMNAS =================
            # Función para ordenar al hacer click en encabezados
            def ordenar(col, reverse):
                data = [(tree.set(k, col), k) for k in tree.get_children("")]
                data.sort(reverse=reverse)
                for index, (_, k) in enumerate(data):
                    tree.move(k, "", index)
                tree.heading(col, command=lambda: ordenar(col, not reverse))

            for col in ("Id", "Nombre", "Ciudad", "Estado"):
                tree.heading(col, text=col, command=lambda c=col: ordenar(c, False))

            # Ancho y alineación de columnas
            tree.column("Id", width=80, anchor=CENTER)
            tree.column("Nombre", width=240)
            tree.column("Ciudad", width=180)
            tree.column("Estado", width=140, anchor=CENTER)

            # ================= CARGA DE DATOS (READ) =================
            # Efecto de filas alternadas
            tree.tag_configure("odd", background="#f9f9f9")
            tree.tag_configure("even", background="#e9eef3")
            tree.tag_configure("hover", background="#dbe9f6")

            for index, row in enumerate(proyectos.mostar_proyectos()):
                tag = "even" if index % 2 == 0 else "odd"
                tree.insert("", END, values=row, tags=(tag,))

            # Evento hover (solo visual)
            def on_motion(event):
                row_id = tree.identify_row(event.y)
                for item in tree.get_children():
                    tree.item(item, tags=("even" if int(tree.index(item)) % 2 == 0 else "odd",))
                if row_id:
                    tree.item(row_id, tags=("hover",))

            tree.bind("<Motion>", on_motion)

            # Evento al seleccionar fila
            tree.bind("<<TreeviewSelect>>", seleccionar_registro)
            tree.pack()

            # Inicia la aplicación
            base.mainloop()

        except Exception as error:
            print(f"Error al mostrar la interfaz: {error}")


# ================= FUNCIONES CRUD =================

def guardar_registro():
    """
    CREATE:
    Inserta un nuevo proyecto en la base de datos
    """
    global texBoxNombre, texBoxCiudad, combo

    try:
        if texBoxNombre is None or texBoxCiudad is None or combo is None:
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
    """
    READ:
    Refresca los datos del Treeview
    """
    global tree
    try:
        tree.delete(*tree.get_children())
        for row in proyectos.mostar_proyectos():
            tree.insert("", "end", values=row)
    except ValueError as error:
        print(f"Error al actualizar tabla {error}")


def seleccionar_registro(event):
    """
    Al seleccionar una fila, se cargan los datos en el formulario
    """
    try:
        item = tree.focus()
        if item:
            values = tree.item(item)['values']
            texBoxId.delete(0, END)
            texBoxId.insert(0, values[0])
            texBoxNombre.delete(0, END)
            texBoxNombre.insert(0, values[1])
            texBoxCiudad.delete(0, END)
            texBoxCiudad.insert(0, values[2])
            combo.set(values[3])
    except ValueError as error:
        print(f"Error al seleccionar registro {error}")


def modificar_registro():
    """
    UPDATE:
    Actualiza un proyecto existente
    """
    global texBoxId, texBoxNombre, texBoxCiudad, combo

    try:
        idproyecto = texBoxId.get()
        nombre = texBoxNombre.get()
        ciudad = texBoxCiudad.get()
        estado = combo.get()

        proyectos.modificar_proyectos(idproyecto, nombre, ciudad, estado)

        messagebox.showinfo("Información", "Los datos fueron actualizados")
        actualizar_treeview()

    except ValueError as error:
        print(f"Error al modificar los datos: {error}")


def eliminar_registro():
    """
    DELETE:
    Elimina un proyecto por ID
    """
    global texBoxId

    try:
        idproyecto = texBoxId.get()
        proyectos.eliminar_proyectos(idproyecto)

        messagebox.showinfo("Información", "Los datos fueron eliminados")
        actualizar_treeview()

    except ValueError as error:
        print(f"Error al eliminar los datos: {error}")


# ================= EJECUCIÓN =================
ProyectosMarval.proyecto_marval()



