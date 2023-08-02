from ConexionBD import Conexion
import psycopg2

class M_Cliente(Conexion):
	def listar_clientes(self):
        self.conectar()
        cursor = self.conexion_activa.cursor()
        try: # Trata de obtener todos los clientes
            cursor.execute("SELECT * FROM Cliente;")
            self.conexion_activa.commit()
            usuarios = cursor.fetchall()
            cursor.close()
            self.desconectar()
            return usuarios  
        except: # Si no lo logra cierra la conexion y lanza una excepcion
            cursor.close()
            self.desconectar()
            raise Exception("Error al acceder a base de datos.")