from ConexionBD.conexion import Conexion
import psycopg2

# =======================================================================
# 	CLASE M_PEDIDO
#		Es con el que se maneja la lectura, insercion y manipulacion
#		de datos en la Base de Datos. Ademas, aqui se genera la Screenshot
#		de la orden
# =======================================================================
class M_Pedido(Conexion):
	def insertar_pedido(self, municipio, ciudad, n_hamburg, monto_deliv, monto_t, metodo_p, estado_d, fecha, cedula, remarks):
            self.conectar()
            cursor = self.conexion_activa.cursor()
            try: # Trata de insertar un cliente
                cursor.execute("INSERT INTO pedido (municipio, ciudad, cant_hamburguesas, m_delivery, m_total, metodo_pago, estado, fecha, cedula_cliente, remarks) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",[municipio, ciudad, n_hamburg, monto_deliv, monto_t, metodo_p, estado_d, fecha, cedula,remarks])
                self.conexion_activa.commit()
                cursor.close()
                self.desconectar()
                print("Insercion exitosa")
            except:
                cursor.close()
                self.desconectar()

	def cambiar_estado_pedido(self,id,estado):
			self.conectar()
			cursor = self.conexion_activa.cursor()
			try: # Trata de insertar un cliente
				cursor.execute("UPDATE pedido SET estado=%s WHERE id=%s;",[estado,id])
				self.conexion_activa.commit()
				cursor.close()
				self.desconectar()
				print("Insercion exitosa")
			except:
				cursor.close()
				self.desconectar()

	def buscar_pedido(self, id):
           self.conectar()
           cursor = self.conexion_activa.cursor()
           try: # Trata de buscar un pedido por id
                cursor.execute("SELECT * FROM pedido WHERE id = %s;",[id])
                self.conexion_activa.commit()
                retornable = cursor.fetchall()
                cursor.close()
                self.desconectar()
                return retornable
           except:
                cursor.close()
                self.desconectar()

	def screenshot(self, id, bytes_imagen):
		self.conectar()
		cursor = self.conexion_activa.cursor()
		try:
			cursor.execute("UPDATE pedido SET screenshot = %s WHERE id = %s",[bytes_imagen, id])
			self.conexion_activa.commit()
			cursor.close()
			self.desconectar()
		except:
			cursor.close()
			self.desconectar()

	def listar_pedidos(self):
		self.conectar()
		cursor = self.conexion_activa.cursor()
		try:
			cursor.execute("SELECT * FROM pedido")
			self.conexion_activa.commit()
			retornable = cursor.fetchall()
			cursor.close()
			self.desconectar()
			return retornable
		except:
			cursor.close()
			self.desconectar()

	def realizar_query_preconstruida(self, query_sql):
		self.conectar()
		cursor = self.conexion_activa.cursor()
		try:
			cursor.execute(query_sql)
			self.conexion_activa.commit()
			retornable = cursor.fetchall()
			cursor.close()
			self.desconectar()
			return retornable
		except:
			cursor.close()
			self.desconectar()