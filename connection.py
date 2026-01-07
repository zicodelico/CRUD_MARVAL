import mysql.connector

# Conexión a la base de datos

class cconexion:
    def Conexion_base_de_datos():
        
        try:
            conexion = mysql.connector.connect(
                host="127.0.0.1",       # Cambia si tu servidor MySQL está en otra máquina
                user="root",      # Usuario de MySQL
                password="kari123",  # Contraseña de MySQL
                database="proyectosmarval",  # Nombre de la base de datos
                port='3306')
            print("conexion correcta")

            return conexion
            
        except mysql.connector.Error as error:
            print("Error al conectar a la base de Datos{}".format(error))
            
            return conexion
        

    Conexion_base_de_datos()




