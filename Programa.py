from Manejador import M_Clientes, Validar
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
@Dir.route("/customers")
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
        if(not(Validar.Validar_Cliente(cliente_json))):
            print("Datos de JSON no validos.")
            abort(400)
        cc.modificar_cliente(cedula,dict_cliente["name"],dict_cliente["email"],dict_cliente["whatsapp"])
        return '', 200
    else:
        print("Error en JSON de entrada")
        abort(400)

#-------------------------------------------------
# SECCION: Manejo de Ordenes
#-------------------------------------------------
#@Dir.route("/orders",methods=["POST"])
#def crear_pedido():

#@Dir.route("/orders/<id>/status", methods = ["PATCH"])
#def estado_pedido(id_pedido):

#@Dir.route("/orders/<id>/payment-screenshot", methods = ["POST"])
#def pedido_screenshot(id_pedido):

#@Dir.route("/orders")
#def mostrar_pedidos():

def pagina_no_encontrada(error):
    return "<h1>Error 404<h2><h2>Página no encontrada</h2>"

if __name__=="__main__":
    Dir.register_error_handler(404,pagina_no_encontrada)
    Dir.run()