#===========================================================================================================
# 	METODOS DE VALIDACIONES
#		Si bien la base de datos tiene sus "Constraint", se hacen validaciones para rechazar solicitudes desde
#		la API
#===========================================================================================================

#>>>>>>>> VALIDACIONES PARA INPUT DE CLIENTES

def Validar_Cliente(cliente):
	if (cliente['cedula'] < 0):
		return False
	if (len(cliente['name']) > 12):
		return False
	numero_telefono_valido = True
	for C in cliente['whatsapp'][1:]:
		if not C.isdigit():
			numero_telefono_valido = False
			break
	if (not(len(cliente['whatsapp']) <= 20 and cliente['whatsapp'][:1] == "+" and numero_telefono_valido)):
		return False
	return True

def Validar_Modif_Cliente(cliente):
	if (len(cliente['name']) > 12):
		return False
	numero_telefono_valido = True
	for C in cliente['whatsapp'][1:]:
		if not C.isdigit():
			numero_telefono_valido = False
			break
	if (not(len(cliente['whatsapp']) <= 20 and cliente['whatsapp'][:1] == "+" and numero_telefono_valido)):
		return False
	return True

#>>>>>>>> VALIDACIONES PARA INPUT DE PEDIDOS

def validar_diccionario_pedidos(dict_pd):
    try:
        int(dict_pd['quantity'])
    except:
        return False
    largo_prueba = len(dict_pd['payment_method'])
    if largo_prueba == 0 or largo_prueba > 10:
        return False
    largo_prueba = len(dict_pd['remarks'])
    if largo_prueba == 0 or largo_prueba > 80:
        return False
    largo_prueba = len(dict_pd['city'])
    if largo_prueba == 0 or largo_prueba > 40:
        return False
    largo_prueba = len(dict_pd['municipality'])
    if largo_prueba == 0 or largo_prueba > 40:
        return False
    largo_prueba = len(dict_pd['cedula'])
    if largo_prueba == 0 or largo_prueba > 12:
        return False
    try:
        int(dict_pd['cedula'])
    except:
        return False
    return True
