from ConexionBD.conexion import Conexion
import psycopg2

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