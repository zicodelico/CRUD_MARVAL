# Importa todo lo definido en connection.py
# Aquí se obtiene la clase cconexion y el acceso a mysql.connector
from connection import *

# Clase que representa la CAPA DE MODELO del CRUD
# Aquí vive toda la lógica de acceso a datos (Base de Datos)
class proyectos: 

    # =========================
    # READ – MOSTRAR PROYECTOS
    # =========================
    def mostar_proyectos():
        """
        FUNCIÓN READ (SELECT)
        OBJETIVO:
        - Consultar todos los registros de la tabla 'proyectos'
        - Retornar los datos para que la interfaz los muestre

        ESTA FUNCIÓN:
        - No recibe parámetros
        - Devuelve una lista de tuplas (registros)
        """
        try:
            # 1. Abrir conexión a la base de datos
            cone = cconexion.Conexion_base_de_datos()

            # 2. Crear cursor para ejecutar sentencias SQL
            cursor = cone.cursor()

            # 3. Ejecutar consulta SELECT
            cursor.execute  ("select * from proyectos;")

            # 4. Obtener todos los resultados de la consulta
            miresultado = cursor.fetchall()

            # 5. Commit (no es necesario para SELECT, pero no rompe)
            cone.commit()

            # 6. Cerrar conexión para liberar recursos
            cone.close()

            # 7. Retornar los datos a quien llamó la función
            return miresultado

        except mysql.connector.Error as error:
            # Manejo de errores de base de datos
            print("Error de mostrar datos{}".format(error))



    # =========================
    # CREATE – INGRESAR PROYECTO
    # =========================
    def ingresar_proyectos(Nombre,Ciudad,Estado):
        """
        FUNCIÓN CREATE (INSERT)
        OBJETIVO:
        - Insertar un nuevo proyecto en la base de datos

        PARÁMETROS:
        - Nombre: nombre del proyecto
        - Ciudad: ciudad del proyecto
        - Estado: estado del proyecto
        """
        try:
            # 1. Abrir conexión a la base de datos
            cone = cconexion.Conexion_base_de_datos()

            # 2. Crear cursor
            cursor = cone.cursor()

            # 3. Definir sentencia SQL INSERT
            # null se usa para que el ID sea autoincremental
            sql = "insert into proyectos values(null,%s,%s,%s);"

            # 4. Valores que reemplazan los %s
            valores = (Nombre,Ciudad,Estado)

            # 5. Ejecutar la sentencia con parámetros
            cursor.execute(sql,valores)

            # 6. Confirmar la transacción (OBLIGATORIO en INSERT)
            cone.commit()

            # 7. Mostrar cuántos registros se insertaron
            print(cursor.rowcount,"Registro ingresado")

            # 8. Cerrar conexión
            cone.close()

        except mysql.connector.Error as error:
            # Manejo de errores al insertar datos
            print("Error de ingreso de datos{}".format(error))


    # =========================
    # UPDATE – MODIFICAR PROYECTO
    # =========================
    def modificar_proyectos(idproyecto,Nombre,Ciudad,Estado):
        """
        FUNCIÓN UPDATE
        OBJETIVO:
        - Modificar un proyecto existente usando su ID

        PARÁMETROS:
        - idproyecto: identificador del proyecto
        - Nombre: nuevo nombre
        - Ciudad: nueva ciudad
        - Estado: nuevo estado
        """
        try:
            # 1. Abrir conexión a la base de datos
            cone = cconexion.Conexion_base_de_datos()

            # 2. Crear cursor
            cursor = cone.cursor()

            # 3. Sentencia SQL UPDATE
            # Actualiza nombre, ciudad y estado según el ID
            sql = "update proyectos set proyectos.nombre = %s,proyectos.ciudad = %s,proyectos.estado = %swhere proyectos.Id_del_Proyecto =%s ;"

            # 4. Valores para la consulta
            valores = (Nombre,Ciudad,Estado,idproyecto)

            # 5. Ejecutar UPDATE
            cursor.execute(sql,valores)

            # 6. Confirmar cambios en la base de datos
            cone.commit()

            # 7. Mostrar cuántos registros fueron modificados
            print(cursor.rowcount,"Registro Actualizado")

            # 8. Cerrar conexión
            cone.close()

        except mysql.connector.Error as error:
            # Manejo de errores al actualizar
            print("Error de actualizacion de datos{}".format(error))


    # =========================
    # DELETE – ELIMINAR PROYECTO
    # =========================
    def eliminar_proyectos(idproyecto):
        """
        FUNCIÓN DELETE
        OBJETIVO:
        - Eliminar un proyecto usando su ID

        PARÁMETRO:
        - idproyecto: identificador único del proyecto
        """
        try:
            # 1. Abrir conexión a la base de datos
            cone = cconexion.Conexion_base_de_datos()

            # 2. Crear cursor
            cursor = cone.cursor()

            # 3. Sentencia SQL DELETE
            sql = "delete from proyectos where proyectos.Id_del_Proyecto =%s;"

            # 4. El ID debe ir en una tupla
            valores = (idproyecto,)

            # 5. Ejecutar DELETE
            cursor.execute(sql,valores)

            # 6. Confirmar eliminación
            cone.commit()

            # 7. Mostrar cuántos registros se eliminaron
            print(cursor.rowcount,"Registro Eliminado")

            # 8. Cerrar conexión
            cone.close()

        except mysql.connector.Error as error:
            # Manejo de errores al eliminar
            print("Error de eliminacion de datos{}".format(error))

