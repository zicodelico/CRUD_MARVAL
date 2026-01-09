from connection import *

class proyectos: 

    def mostar_proyectos():
        try:
            cone = cconexion.Conexion_base_de_datos()
            cursor = cone.cursor()
            cursor.execute  ("select * from proyectos;")
            miresultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miresultado

        except mysql.connector.Error as error:
            print("Error de mostrar datos{}".format(error))



    def ingresar_proyectos(Nombre,Ciudad,Estado):

        try:
            cone = cconexion.Conexion_base_de_datos()
            cursor = cone.cursor()
            sql = "insert into proyectos values(null,%s,%s,%s);"
            valores = (Nombre,Ciudad,Estado)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()




        except mysql.connector.Error as error:
            print("Error de ingreso de datos{}".format(error))


    def modificar_proyectos(idproyecto,Nombre,Ciudad,Estado):

        try:
            cone = cconexion.Conexion_base_de_datos()
            cursor = cone.cursor()
            sql = "update proyectos set proyectos.nombre = %s,proyectos.ciudad = %s,proyectos.estado = %swhere proyectos.Id_del_Proyecto =%s ;"
            valores = (Nombre,Ciudad,Estado,idproyecto)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()




        except mysql.connector.Error as error:
            print("Error de actualizacion de datos{}".format(error))


    def eliminar_proyectos(idproyecto):

        try:
            cone = cconexion.Conexion_base_de_datos()
            cursor = cone.cursor()
            sql = "delete from proyectos where proyectos.Id_del_Proyecto =%s;"
            valores = (idproyecto,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            cone.close()




        except mysql.connector.Error as error:
            print("Error de eliminacion de datos{}".format(error))
