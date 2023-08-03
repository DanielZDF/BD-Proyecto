from Manejador import M_Clientes, M_Pedidos, Validar
from flask import Flask, abort, jsonify, request
import psycopg2
import datetime

Dir = Flask(__name__)

@Dir.route("/home")
def route():
    return "<h1>Ayo</h1>"

#-------------------------------------------------
# SECCION: Manejo de Clientes
#-------------------------------------------------
@Dir.route("/customers", methods = ["GET"])
def mostrar_clientes():
    cc = M_Clientes.M_Cliente()
    lista_clientes = cc.listar_clientes()
    clientes = []
    if lista_clientes != None:
        for instancia in lista_clientes:
            diccionario_cliente = {"cedula":instancia[0],"name":instancia[1],"whatsapp":instancia[2],"email":instancia[3]}
            clientes.append(diccionario_cliente)
    return jsonify(clientes),200

@Dir.route("/customers", methods = ["POST"])
def crear_cliente():
    cc = M_Clientes.M_Cliente()
    cliente_json = request.get_json()
    if {'cedula','name','email','whatsapp'} <= set(cliente_json):
        Archivo_Valido = Validar.Validar_Cliente(cliente_json)
        if (Archivo_Valido):
            cc.insertar_cliente(cliente_json['cedula'] ,cliente_json['name'], cliente_json['email'], cliente_json['whatsapp'])
            return cliente_json,201
        else:
            print("Datos de JSON no validos.")
            abort(400)
    else:
        print("Error en JSON de entrada")
        abort(400)

@Dir.route("/customers/<cedula>",methods = ["PUT"])
def modificar_cliente(cedula):
    cc = M_Clientes.M_Cliente()
    cliente_json = request.get_json()
    if (cc.obtener_cliente(cedula) == None):
        print("No existe el cliente")
        abort(404)
    if {'name','email','whatsapp'} <= set(cliente_json):
        if(not(Validar.Validar_Modif_Cliente(cliente_json))):
            print("Datos de JSON no validos.")
            abort(400)
        cc.modificar_cliente(cedula,cliente_json["name"],cliente_json["email"],cliente_json["whatsapp"])
        return '', 200
    else:
        print("Error en JSON de entrada")
        abort(400)

#-------------------------------------------------
# SECCION: Manejo de Ordenes
#-------------------------------------------------
@Dir.route("/orders",methods=["POST"])
def crear_pedido():
    orden_json = request.get_json()
    if {'quantity','payment_method','remarks','city','municipality','cedula'} <= set(orden_json):
        cc = M_Clientes.M_Cliente()
        if (cc.obtener_cliente(orden_json['cedula']) == None):
            print("No existe el cliente")
            abort(404)
        if(not Validar.validar_diccionario_pedidos(orden_json)):
            print("Datos de JSON no validos.")
            abort(400)
        if orden_json['municipality'].lower() != 'maneiro':
            monto_envio = 2.00
        else:
            monto_envio = 0
        n_hamburguesas = int(orden_json['quantity'])
        monto_t = (n_hamburguesas*5) + monto_envio
        fecha = datetime.datetime.now()
        estado_d = 'pending'
        conexion = M_Pedidos.M_Pedido()
        conexion.insertar_pedido(orden_json['municipality'], orden_json['city'], n_hamburguesas, monto_envio, monto_t, orden_json['payment_method'], estado_d, fecha, orden_json['cedula'], orden_json['remarks'])
        return '', 200
    else:
        print("Error en JSON de entrada")
        abort(400)

@Dir.route("/orders/<id>/status", methods = ["PATCH"])
def estado_pedido(id):
    orden_json = request.get_json()
    if(not Validar.validar_estado(orden_json)):
        print("Datos de JSON no validos.")
        abort(400)
    cc = M_Pedidos.M_Pedido()
    if (cc.buscar_pedido(id) == []):
        print("No existe el pedido")
        abort(404)
    estado = orden_json['status']
    print(id)
    print(estado)
    cc.cambiar_estado_pedido(id,estado)
    return '', 200


@Dir.route("/orders/<id_pedido>/payment-screenshot", methods = ["POST"])
def pedido_screenshot(id_pedido):
    archivo = request.files['screenshot']
    bytes_imagen = archivo.read()
    cc = M_Pedidos.M_Pedido()
    if (cc.buscar_pedido(id) == []):
        print("No existe el pedido")
        abort(404)
    print(id_pedido)
    cc.screenshot(id_pedido,bytes_imagen)
    return '',201

@Dir.route("/orders", methods = ["GET"])
def mostrar_pedidos():
    conexion = M_Pedidos.M_Pedido()
    retornable = []
    if (request.args.to_dict() == {}):
        lista_tuplas = conexion.listar_pedidos()
    else:
        dict_args = request.args.to_dict()
        segmento_where = ""
        #if 'cedula' in dict_args:
            #condicion = dict_args['cedula']
            #segmento_where = segmento_where + "cedula = '" + condicion + "' AND "
        if 'status' in dict_args:
            condicion= dict_args['status']
            segmento_where = segmento_where + "estado = '" + condicion + "' AND "
        #if 'date' in dict_args:
            #condicion = dict_args['date']
            #segmento_where = segmento_where + "fecha = '" + condicion + "' AND "
        #segmento_where = segmento_where[:-5] + ";"
        query = f"SELECT * FROM pedido WHERE {segmento_where}"
        lista_tuplas = conexion.realizar_query_preconstruida(query)
    if lista_tuplas != []:
        for tup in lista_tuplas:
            dict_ped = {}
            dict_ped['id'] = tup[0]
            dict_ped['cedula'] = tup[1]
            dict_ped['quantity'] = tup[2]
            dict_ped['delivery_amount'] = tup[3]
            dict_ped['total'] = tup[4]
            dict_ped['status'] = tup[5]
            dict_ped['datetime'] = tup[6]
            dict_ped['payment_method'] = tup[7]
            screen = tup[8]
            if screen is not None:
                dict_ped['screenshot'] = screen.hex()
            else:
                dict_ped['screenshot'] = screen
            dict_ped['municipality'] = tup[9]
            dict_ped['city'] = tup[10] 
            dict_ped['remark'] = tup[11]
            retornable.append(dict_ped)
    return jsonify(retornable), 200

def pagina_no_encontrada(error):
    return "<h1>Error 404<h2><h2>Página no encontrada</h2>"

if __name__=="__main__":
    Dir.register_error_handler(404,pagina_no_encontrada)
    Dir.run()