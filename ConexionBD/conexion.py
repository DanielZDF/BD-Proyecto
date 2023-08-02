from ConexionBD.configuracion import Config
import psycopg2

class Conexion:
    def __init__(self):
        self.user = Config.POSTGRES_USER
        self.password = Config.POSTGRES_PASSWORD
        self.port = Config.POSTGRES_PORT
        self.database = Config.POSTGRES_DB
        self.host = Config.POSTGRES_HOST
        self.conexion_activa = None

    def conectar(self):
        if self.conexion_activa != None:
            raise Exception("Ya hay un conexión activa.")
        else:
            conex = psycopg2.connect(dbname = self.database, user = self.user, password = self.password, host = self.host, port = self.port)
            print('Conexion exitosa')
            self.conexion_activa = conex

    def desconectar(self):
        if self.conexion_activa == None:
            raise Exception("No hay conexion activa")
        else:
            self.conexion_activa.close()
            print('Desconexion exitosa')
            self.conexion_activa = None


