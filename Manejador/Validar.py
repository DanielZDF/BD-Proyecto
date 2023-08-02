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