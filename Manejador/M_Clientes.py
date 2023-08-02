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
			cursor.execute("INSERT INTO public.cliente(cedula, nombre, whatsapp, email) VALUES (ced, nom, what, em);"),
			self.conexion_activa.commit()
			cursor.close()
			self.desconectar()
			print("Insercion exitosa.")
		except:
			cursor.close()
			self.desconectar()
			raise Exception("Error al insertar el cliente en la base de datos, verifique que la cedula de un cliente no se repita")     