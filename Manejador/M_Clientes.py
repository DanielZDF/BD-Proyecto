from ConexionBD.conexion import Conexion
import psycopg2

# =======================================================================
# 	CLASE M_CLIENTE
#		Es con el que se maneja la lectura, insercion y manipulacion
#		de datos en la Base de Datos
# =======================================================================
class M_Cliente(Conexion):
	# -------------------------------------------------------------------
	# METODO PARA LISTAR CLIENTES
	# -------------------------------------------------------------------
	def listar_clientes(self):
		self.conectar()
		cursor = self.conexion_activa.cursor()
		try:
			cursor.execute("SELECT * FROM cliente ORDER BY cedula ASC;")
			self.conexion_activa.commit()
			lista_clientes = cursor.fetchall()
			cursor.close()
			self.desconectar()
			return lista_clientes  
		except: 
			cursor.close()
			self.desconectar()
			raise Exception("Error al acceder a base de datos.")
	# -------------------------------------------------------------------
	# METODO PARA INSERTAR CLIENTES
	# -------------------------------------------------------------------
	def insertar_cliente(self, cedula, nombre_completo, email, whatsapp):
        self.conectar()
        cursor = self.conexion_activa.cursor()
        try:
            cursor.execute("INSERT INTO Cliente VALUES (%s,%s,%s,%s);",(cedula, nombre_completo,email,whatsapp))
            self.conexion_activa.commit()
            cursor.close()
            self.desconectar()
        except:
            cursor.close()
            self.desconectar()    