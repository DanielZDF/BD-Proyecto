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
	def insertar_cliente(self, ced, nom, em, what):
		self.conectar()
		cursor = self.conexion_activa.cursor()
		try:
			cursor.execute("INSERT INTO cliente VALUES (%s,%s,%s,%s);",(ced,nom,what,em))
			self.conexion_activa.commit()
			cursor.close()
			self.desconectar()
			print("Insercion exitosa.")
		except:
			cursor.close()
			self.desconectar()
			raise Exception("ERROR EN LA INSERCION")

	def obtener_cliente(self,cedula):
		self.conectar()
		cursor = self.conexion_activa.cursor()
		try:
			cursor.execute("SELECT * FROM cliente WHERE cedula=%s",[cedula])
			self.conexion_activa.commit()
			cliente = cursor.fetchone()
			cursor.close()
			self.desconectar()
			return cliente
		except:
			cursor.close()
			self.desconectar()
			raise Exception("ERROR EN LA QUERY")

	def modificar_cliente(self, ced, nom, em, what):
		self.conectar()
		cursor = self.conexion_activa.cursor()
		try:
			cursor.execute("UPDATE cliente SET nombre = %s, whatsapp = %s, email = %s WHERE cedula = %s",[nom, what, em, ced])
			self.conexion_activa.commit()
			cursor.close()
			self.desconectar()
			print("Insercion exitosa.")
		except:
			cursor.close()
			self.desconectar()
			raise Exception("ERROR EN LA INSERCION")
