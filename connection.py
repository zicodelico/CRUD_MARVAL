# Importa el conector oficial de MySQL para Python
# Este módulo permite conectarse, ejecutar consultas y manejar transacciones
import mysql.connector


# ==========================================
# CLASE DE CONEXIÓN A BASE DE DATOS
# ==========================================
# Esta clase pertenece a la CAPA DE ACCESO A DATOS
# Su única responsabilidad es crear y devolver una conexión a MySQL
class cconexion:

    def Conexion_base_de_datos():
        """
        FUNCIÓN DE CONEXIÓN A BASE DE DATOS

        OBJETIVO:
        - Establecer conexión con el servidor MySQL
        - Retornar el objeto conexión para ser usado por otras capas

        ESTA FUNCIÓN:
        - No recibe parámetros
        - Usa credenciales fijas
        - Devuelve un objeto de tipo mysql.connector.connection
        """
        
        try:
            # ==========================================
            # CREACIÓN DEL OBJETO CONEXIÓN
            # ==========================================
            # mysql.connector.connect() establece la conexión física
            conexion = mysql.connector.connect(
                host="127.0.0.1",       # Dirección del servidor MySQL (localhost)
                user="root",            # Usuario de MySQL
                password="kari123",     # Contraseña del usuario
                database="proyectosmarval",  # Base de datos a utilizar
                port='3306'             # Puerto por defecto de MySQL
            )

            # Mensaje de confirmación en consola
            # Útil para depuración durante desarrollo
            print("conexion correcta")

            # Retorna la conexión activa
            return conexion
            
        except mysql.connector.Error as error:
            # ==========================================
            # MANEJO DE ERRORES DE CONEXIÓN
            # ==========================================
            # Captura errores como:
            # - Usuario o contraseña incorrectos
            # - Base de datos inexistente
            # - Servidor apagado
            # - Puerto incorrecto
            print("Error al conectar a la base de Datos{}".format(error))
            
            # Retorna la variable conexion
            # (en este punto puede no estar inicializada)
            return conexion
        

    # ==========================================
    # EJECUCIÓN AUTOMÁTICA DEL MÉTODO
    # ==========================================
    # Esta línea ejecuta la conexión apenas se importa el archivo
    # Sirve para comprobar que la base de datos está disponible
    Conexion_base_de_datos()





