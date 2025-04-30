nombre = "USUARIO"
columnas = {"USUARIO": [{"Nombre Completo": "nombreCompleto"},
                        {"Correo Electrónico": "correoElectronico"},
                        {"Contraseña": "contrasena"}],
            
            "PRODUCTO": [{"Nombre": "nombre"},
                            {"Descripción": "descripcion"},
                            {"Precio": "precio"},
                            {"Inventario": "inventario"},
                            {"Proveedor": "idProveedor"}],
            
            "PROVEEDOR": [{"Razón Social": "razonSocial"},
                            {"RFC": "rfc"},
                            {"Correo Electrónico": "correo"},
                            {"Teléfono": "telefono"}]
            }

valores = [0, 1, 2, 3]
print([valor for valor in valores[:-1]])