# Crear método de borrado, crear interfaz de PROVEEDOR

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from typing import List
import re, sys, math

columnas = {"USUARIO": [{"Id": "idUsuario"},
                        {"Nombre Completo": "nombreCompleto"},
                        {"Correo Electrónico": "correoElectronico"}, # Validar formato y unicidad
                        {"Contraseña": "contrasena"}], # Validar semejanza con "Repetir contraseña"
            
            "PRODUCTO": [{"Id": "idProducto"},
                         {"Nombre": "nombre"}, # Validar unicidad en base a nombre y proveedor
                         {"Descripción": "descripcion"},
                         {"Precio": "precio"}, # Validar valores positivos
                         {"Inventario": "inventario"}, # Validar valores positivos
                         {"Proveedor": "idProveedor"}],
            
            "PROVEEDOR": [{"Id": "idProveedor"},
                          {"Nombre": "nombre"},
                          {"Razón Social": "razonSocial"}, # PENDIENTE. Verificar el tipo de campo que se utilizará
                          {"RFC": "rfc"}, # Verificar formato, varía según la razón social
                          {"Correo Electrónico": "correoElectronico"},
                          {"Teléfono": "telefono"}] # Verificar formato
            }

# Centrar ventana en la pantalla
def centrar_ventana(ventana: QWidget):
    qr = ventana.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    ventana.move(qr.topLeft())

# Generar ventana emergente
def ventana_dialogo(titulo: str, texto: str, tipo: QMessageBox.Icon):
    mensaje = QMessageBox()
    mensaje.setIcon(tipo)
    mensaje.setWindowTitle(titulo)
    mensaje.setText(texto)
    mensaje.exec_()

# Validación de correo para consultas
def validacion_correo_texto(texto) -> bool:
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(patron, texto):
        return True
        
    else:
        return False

def validacion_rfc_texto(texto, persona) -> bool:
    patron_fisica = r'^[A-ZÑ&]{4}\d{6}[A-Z0-9]{3}$'
    patron_moral = r'^[A-ZÑ&]{3}\d{6}[A-Z0-9]{3}$'
    
    if persona == "Persona Física":
        if re.match(patron_fisica, texto):
            return True
        
        else:
            return False
        
    else:
        if re.match(patron_moral, texto):
            return True
        
        else:
            return False

# Activar botón Limpiar
def activar_boton_any(widgets: List[QWidget], boton: QPushButton):
    estado = any(
        (isinstance(widget, QLineEdit) and widget.text().strip() != "") or
        (isinstance(widget, QRadioButton) and widget.isChecked())
        for widget in widgets
    )
    
    boton.setEnabled(estado)

def conexion_LineEdit_PushButton_any(widgets: List[QWidget], boton: QPushButton):
    for widget in widgets:
        if isinstance(widget, QLineEdit):
            widget.textChanged.connect(lambda _, ws = widgets, b = boton: activar_boton_any(ws, b))
            
        elif isinstance(widget, QRadioButton):
            widget.toggled.connect(lambda _, ws = widgets, b = boton: activar_boton_any(ws, b))
        
    activar_boton_any(widgets, boton)

# Activar botón de acción
def activar_boton_all(widgets: List[QWidget], boton: QPushButton):
    line_edits = [w for w in widgets if isinstance(w, QLineEdit)]
    radio_buttons = [w for w in widgets if isinstance(w, QRadioButton)]

    line_edits_ok = all(w.text().strip() != "" for w in line_edits)

    radio_buttons_ok = True
    if radio_buttons:
        radio_buttons_ok = any(w.isChecked() for w in radio_buttons)

    boton.setEnabled(line_edits_ok and radio_buttons_ok)

def conexion_LineEdit_PushButton_all(widgets: List[QWidget], boton: QPushButton):
    for widget in widgets:
        if isinstance(widget, QLineEdit):
            widget.textChanged.connect(lambda _, ws=widgets, b=boton: activar_boton_all(ws, b))

        elif isinstance(widget, QRadioButton):
            widget.toggled.connect(lambda _, ws=widgets, b=boton: activar_boton_all(ws, b))

    activar_boton_all(widgets, boton)

# Borrar texto en LineEdits
def borrar_contenido(widgets: List[QWidget]):
    for widget in widgets:
        if isinstance(widget, QLineEdit):
            widget.clear()

        elif isinstance(widget, QRadioButton):
            widget.setAutoExclusive(False)
            widget.setChecked(False)
            widget.setAutoExclusive(True)

def conexion_pushButton_borrado(boton: QPushButton, widgets: List[QLineEdit]):
    boton.clicked.connect(lambda: borrar_contenido(widgets))

# Cargar contenido de QTableWidget
def contenido_consulta(widgets: List[QLineEdit], campos: List[str]) -> dict:
    return {campo: widget.text() for campo, widget in zip(campos, widgets)}

# Cambiar páginas de QStackedWidget
def cambiar_indice(parent: QWidget, widget: QStackedWidget, indice: int, conexion) -> bool:
    widget.setCurrentIndex(indice)
    
    nombre = type(parent).__name__[5:].upper()
    
    if indice != 0:
        tablas = {
            1: parent.tableWidget,
            2: parent.tableWidget_2,
            3: parent.tableWidget_3
        }
        
        tabla = tablas.get(indice)
        
        keys = [list(columna.keys())[0] for columna in columnas[nombre]]
        
        tabla.setColumnCount(len(keys)-1)
        tabla.setHorizontalHeaderLabels(keys[1:])
        
        values = [list(columna.values())[0] for columna in columnas[nombre]]
        
        campos = ", ".join(values)
        
        cursor = conexion.cursor()
        cursor.execute(f"SELECT {campos} FROM {nombre} ORDER BY {values[0]} DESC")
        datos = cursor.fetchall()
        
        tabla.setRowCount(len(datos))
        
        if hasattr(parent, 'editando'):
            parent.editando = True
        
        for fila, registro in enumerate(datos):
            for columna, valor in enumerate(registro):
                celda = QTableWidgetItem(str(valor))
                
                if columna != 0:
                    tabla.setItem(fila, columna - 1, celda)
        
        if hasattr(parent, 'editando'):
            parent.editando = False 
        
        if nombre == "PRODUCTO" or nombre == "PROVEEDOR":          
            header = tabla.horizontalHeader()
            header.setStretchLastSection(False)
            
            for i in range(len(keys) - 1):
                header.setSectionResizeMode(i, QHeaderView.Stretch)
                
        return True

def conectar_pushButton_index(parent: QWidget, widget: QStackedWidget, botones: List[QPushButton], conexion):
    for indice, boton in enumerate(botones):
        boton.clicked.connect(lambda _, p = parent, w = widget, i = indice, c = conexion: cambiar_indice(p, w, i, c))

# Agregar registro a la tabla correspondiente
def agregar_registro(parent: QWidget, label: QLabel, widgets: List[QWidget], conexion):
    valores = [
        widget.text()
        for widget in widgets
        if (isinstance(widget, QLineEdit)) or
           (isinstance(widget, QRadioButton) and widget.isChecked()) 
    ]
    
    nombre = type(parent).__name__[5:].upper()
    
    cursor = conexion.cursor()
    
    match nombre:
        case "USUARIO":
            cursor.execute("SELECT COUNT(*) FROM USUARIO WHERE correoElectronico = ?", (valores[1], ))
            
            if not(validacion_correo_texto(valores[1])):
                ventana_dialogo("Correo Inválido", "El formato del correo electrónico es inválido.", QMessageBox.Warning)
                return
            
            elif cursor.fetchone()[0]:
                ventana_dialogo("Correo en Uso", "Actualmente ya hay un usuario registrado con ese correo.", QMessageBox.Warning)
                return
            
            elif valores[2] != valores[3]:
                ventana_dialogo("Contraseñas Distintas", "Las contraseñas no coincide.", QMessageBox.Warning)
                return
        
        case "PRODUCTO":
            bool_producto = cursor.execute("SELECT COUNT(*) FROM PRODUCTO WHERE nombre = ? AND idProveedor = ?", (valores[0], valores[4]))
            bool_proveedor = cursor.execute("SELECT COUNT(*) FROM PROVEEDOR WHERE idProveedor = ?", (valores[4],))

            if bool_producto:
                ventana_dialogo("Producto Existente", "Este producto ya ha sido registrado previamente.", QMessageBox.Warning)
                return
            
            elif int(valores[2]) <= 0:
                ventana_dialogo("Valor Inválido", "El precio del producto debe ser mayor a 0.", QMessageBox.Warning)
                return
            
            elif int(valores[3]) <= 0:
                ventana_dialogo("Valor Inválido", "El inventario del producto debe ser mayor a 0.", QMessageBox.Warning)
                return
            
            elif not(bool_proveedor):
                ventana_dialogo("Proveedor Inexistente", "No hay ningún proveedor registrado con el Id proporcionado.", QMessageBox.Warning)
                return
                
        case "PROVEEDOR":
            bool_rfc = cursor.execute("SELECT COUNT(*) FROM PROVEEDOR WHERE rfc = ?", (valores[2], ))
            bool_correo = cursor.execute("SELECT COUNT(*) FROM PROVEEDOR WHERE correoElectronico = ?", (valores[3], ))
            bool_telefono = cursor.execute("SELECT COUNT(*) FROM PROVEEDOR WHERE telefono = ?", (valores[4], ))
            
            if bool_rfc:
                ventana_dialogo("RFC en Uso", "Actualmente este RFC está en uso.", QMessageBox.Warning)
                return
            
            elif not(validacion_rfc_texto(valores[2], valores[1])):
                ventana_dialogo("RFC Inválido", "El formato del RFC es inválido.", QMessageBox.Warning)
                return
            
            elif bool_correo:
                ventana_dialogo("Correo en Uso", "Actualmente este correo está en uso.", QMessageBox.Warning)
                return
            
            if not(validacion_correo_texto(valores[3])):
                ventana_dialogo("Correo Inválido", "El formato del correo electrónico es inválido.", QMessageBox.Warning)
                return
            
            elif bool_telefono:
                ventana_dialogo("Teléfono en Uso", "Actualmente este teléfono está en uso.", QMessageBox.Warning)
                return
            
            elif len(valores[4]) <= 9 or len(valores[4]) >= 11:
                ventana_dialogo("Teléfono Inválido", "El teléfono debe poseer 10 caracteres.", QMessageBox.Warning)
                return
    
    keys = [list(columna.keys())[0] for columna in columnas[nombre][1:]]
    values = [list(columna.values())[0] for columna in columnas[nombre][1:]]
    
    
    placeholders = ", ".join(["?" for _ in range(len(columnas[nombre]) - 1)])
    campos = ", ".join(values)
        
    if nombre == "USUARIO":
        cursor.execute(f"INSERT INTO {nombre} ({campos}) VALUES ({placeholders})", tuple(valores[:-1]))
        
    else:
        cursor.execute(f"INSERT INTO {nombre} ({campos}) VALUES ({placeholders})", tuple(valores))
        
    conexion.commit()
    
    QMessageBox.information(parent, "Éxito", f"El {nombre.lower()} se ha registrado exitosamente.")
    
    label.setText(f"ID del Usuario: {cursor.lastrowid + 1}")
    
    borrar_contenido(widgets)

# Actualizar registro a la tabla correspondiente
def actualizar_registro(parent, tabla: QTableWidget, fila: int, columna: int, conexion):
    nombre_tabla = type(parent).__name__[5:].upper()
    campo_id = list(columnas[nombre_tabla][0].values())[0]
    campo = list(columnas[nombre_tabla][columna + 1].values())[0]
    valor = tabla.item(fila, columna).text()

    if nombre_tabla == "PROVEEDOR" and columna == 2:
        razon_social = tabla.item(fila, columna - 1).text()
    
    cursor = conexion.cursor()
    
    lista_ids = []
    cursor.execute(f"SELECT * FROM {nombre_tabla} ORDER BY 1 DESC")
    lista_ids = [registro[0] for registro in cursor.fetchall()]
    
    campos_numéricos = ["precio", "inventario", "idProveedor", "telefono"]
    
    if campo == "correoElectronico":
        cursor.execute(f"SELECT COUNT(*) FROM {nombre_tabla} WHERE correoElectronico = ?", (valor, ))
        bool_unicidad_correo = cursor.fetchone()[0]
    
    elif campo == "idProveedor":
        cursor.execute(f"SELECT COUNT(*) FROM PROVEEDOR WHERE idProveedor = ?", (valor, ))
        bool_proveedor_existente = cursor.fetchone()[0]
        
    elif campo == "telefono":
        cursor.execute(f"SELECT COUNT(*) FROM {nombre_tabla} WHERE telefono = ?", (valor, ))
        bool_unicidad_telefono = cursor.fetchone()[0]
        
    elif campo == "rfc":
        cursor.execute(f"SELECT COUNT(*) FROM {nombre_tabla} WHERE rfc = ?", (valor, ))
        bool_unicidad_rfc = cursor.fetchone()[0]
    
    if not(valor):
        ventana_dialogo("Campo Vacío", "Asigne algún valor al campo.", QMessageBox.Warning)
        return
    
    elif (campo in campos_numéricos) and (not(valor.replace(".", "", 1).isdigit())):
        ventana_dialogo("Valor Inválido", "Este campo solo acepta valores numéricos.", QMessageBox.Warning)
        return
    
    elif (campo in campos_numéricos) and (math.ceil(float(valor)) <= 0):
        ventana_dialogo("Valor Inválido", "El valor debe ser mayor a 0.", QMessageBox.Warning)
        return
    
    elif (campo == "correoElectronico") and (not(validacion_correo_texto(valor))):
        ventana_dialogo("Correo Inválido", "El formato del correo electrónico es inválido.", QMessageBox.Warning)
        return
    
    elif (campo == "correoElectronico") and (bool_unicidad_correo):
        ventana_dialogo("Correo en Uso", "Actualmente este correo está en uso.", QMessageBox.Warning)
        return
    
    elif (campo == "idProveedor") and (not(bool_proveedor_existente)):
        ventana_dialogo("Proovedor Inexistente", "No hay ningún proveedor registrado con el Id proporcionado.", QMessageBox.Warning)
        return
        
    elif (campo == "telefono") and (bool_unicidad_telefono):
        ventana_dialogo("Teléfono en Uso", "Actualmente este teléfono está en uso.", QMessageBox.Warning)
        return
    
    elif (campo == "telefono") and ((len(valor) <= 9) or (len(valor) >= 11)):
        ventana_dialogo("Teléfono Inválido", "El teléfono debe poseer 10 caracteres.", QMessageBox.Warning)
        return
    
    elif (campo == "rfc") and (bool_unicidad_rfc):
        ventana_dialogo("RFC en Uso", "Actualmente este RFC está en uso.", QMessageBox.Warning)
        return
    
    elif (campo == "rfc") and not(validacion_rfc_texto(valor, razon_social)):
        ventana_dialogo("RFC Inválido", "El formato del RFC es inválido.", QMessageBox.Warning)
        return
        
    cursor.execute(f"UPDATE {nombre_tabla} SET {campo} = ? WHERE {campo_id} = ?", (valor, lista_ids[fila]))
    conexion.commit()