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
                raise Exception("Error al insertar un pedido en la base de datos")

    def cambiar_estado_pedido(id,estado):
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
                raise Exception("Error al insertar un pedido en la base de datos")      