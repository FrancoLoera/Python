from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from typing import List
import re, sys

def centrar_ventana(ventana: QWidget):
    qr = ventana.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    ventana.move(qr.topLeft())
    
def validacion_correo_widget(parent: QWidget, line_edit: QLineEdit) -> bool:
    texto = line_edit.text()
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(patron, texto):
        return True
        
    else:
        QMessageBox.warning(
            parent,
            "Correo inválido",
            f"El formato del correo electrónico es inválido."
        )
        return False
    
def validacion_correo_texto(texto) -> bool:
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(patron, texto):
        return True
        
    else:
        ventana_dialogo("Correo Inválido", "El formato del correo electrónico es inválido.", QMessageBox.warning)
        return False

def activar_boton_any(widgets: List[QLineEdit], boton: QPushButton):
    estado = any(widget.text().strip() != "" for widget in widgets)
    boton.setEnabled(estado)

def conexion_LineEdit_PushButton_any(widgets: List[QLineEdit], boton: QPushButton):
    for widget in widgets:
        widget.textChanged.connect(lambda _, ws = widgets, b = boton: activar_boton_any(ws, b))
        
    activar_boton_any(widgets, boton)
    
def activar_boton_all(widgets: List[QLineEdit], boton: QPushButton):
    estado = all(widget.text().strip() != "" for widget in widgets)
    boton.setEnabled(estado)

def conexion_LineEdit_PushButton_all(widgets: List[QLineEdit], boton: QPushButton):
    for widget in widgets:
        widget.textChanged.connect(lambda _, ws = widgets, b = boton: activar_boton_all(ws, b))
        
    activar_boton_all(widgets, boton)

def borrar_contenido(widgets: List[QLineEdit]):
    for widget in widgets:
        widget.clear()

def conexion_pushButton_borrado(boton: QPushButton, widgets: List[QLineEdit]):
    boton.clicked.connect(lambda: borrar_contenido(widgets))
    
def contenido_consulta(widgets: List[QLineEdit], campos: List[str]) -> dict:
    return {campo: widget.text() for campo, widget in zip(campos, widgets)}

def consulta_agregar(widgets: List[QLineEdit], campos: List[str], tabla: str, conexion) -> bool:
    datos = contenido_consulta(widgets, campos)
    columnas = ", ".join(campos)
    placeholders = ", ".join(["?" for _ in campos])
    
    cursor = conexion.cursor()
    
    try:
        cursor.execute(f"INSERT INTO {tabla} ({columnas}) VALUES ({placeholders})", tuple(datos.values()))
        conexion.commit()
        return True
        
    except Exception as e:
        excepcion = sys.exc_info()
        print(f"Error de tipo: {excepcion[0]}. Mensaje del error: {excepcion[1]}")
        
        return False

def cambiar_indice(parent: QWidget, widget: QStackedWidget, indice: int, conexion):
    widget.setCurrentIndex(indice)
    
    nombre = type(parent).__name__[5:].upper()
    columnas = {"USUARIO": [{"Id": "idUsuario"},
                            {"Nombre Completo": "nombreCompleto"},
                            {"Correo Electrónico": "correoElectronico"},
                            {"Contraseña": "contrasena"}],
                
                "PRODUCTO": [{"Id": "idProducto"},
                             {"Nombre": "nombre"},
                             {"Descripción": "descripcion"},
                             {"Precio": "precio"},
                             {"Inventario": "inventario"},
                             {"Proveedor": "idProveedor"}],
                
                "PROVEEDOR": [{"Id": "idProveedor"},
                              {"Razón Social": "razonSocial"},
                              {"RFC": "rfc"},
                              {"Correo Electrónico": "correo"},
                              {"Teléfono": "telefono"}]
                }
    
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
        
        ids = [registro[0] for registro in datos]
        
        for fila, registro in enumerate(datos):
            for columna, valor in enumerate(registro):
                celda = QTableWidgetItem(str(valor))
                
                if columna != 0:
                    tabla.setItem(fila, columna - 1, celda)

def conectar_pushButton_index(parent: QWidget, widget: QStackedWidget, botones: List[QPushButton], conexion):
    for indice, boton in enumerate(botones):
        boton.clicked.connect(lambda _, p = parent, w = widget, i = indice, c = conexion: cambiar_indice(p, w, i, c))

def agregar_registro(parent: QWidget, label: QLabel, widgets: List[QLineEdit], conexion):
    valores = [widget.text() for widget in widgets]
    
    nombre = type(parent).__name__[5:].upper()
            
    columnas = {"USUARIO": [{"Id": "idUsuario"},
                            {"Nombre Completo": "nombreCompleto"},
                            {"Correo Electrónico": "correoElectronico"}, # Validar formato y unicidad
                            {"Contraseña": "contrasena"}], # Validar semejanza con "Repetir contraseña"
                
                "PRODUCTO": [{"Id": "idProducto"},
                             {"Nombre": "nombre"}, # Validar unicidad en base a nombre y proveedor
                             {"Descripción": "descripcion"},
                             {"Precio": "precio"},
                             {"Inventario": "inventario"},
                             {"Proveedor": "idProveedor"}],
                
                "PROVEEDOR": [{"Id": "idProveedor"},
                              {"Razón Social": "razonSocial"}, # PENDIENTE. Verificar el tipo de campo que se utilizará
                              {"RFC": "rfc"}, # Verificar formato, varía según la razón social
                              {"Correo Electrónico": "correo"},
                              {"Teléfono": "telefono"}] # Verificar formato
                }
    
    cursor = conexion.cursor()
    
    match nombre:
        case "USUARIO":
            if not(validacion_correo_texto(valores[1])):
                return
            
            if valores[2].text() != valores[3].text():
                ventana_dialogo("Contraseñas Distintas", "Las contraseñas no coincide.", QMessageBox.warning)
                return
        
        case "PRODUCTO":
            cursor.execute("SELECT COUNT(*) FROM PRODUCTO WHERE nombre = ? AND idProveedor = ?", (valores[0], valores[4]))
            
            if cursor.fetchone()[0]:
                ventana_dialogo("Producto Existente", "Este producto ya ha sido registrado previamente.", QMessageBox.warning)
                
    
    keys = [list(columna.keys())[0] for columna in columnas[nombre][1:]]
    values = [list(columna.values())[0] for columna in columnas[nombre][1:]]
    
    
    placeholders = ", ".join(["?" for _ in range(len(columnas[nombre]) - 1)])
    campos = ", ".join(values)
        
    cursor.execute(f"INSERT INTO {nombre} ({campos}) VALUES ({placeholders})", tuple(valores[:-1]))
    conexion.commit()
    
    QMessageBox.information(parent, "Éxito", f"El {nombre.lower()} se ha registrado exitosamente.")
    
    label.setText(f"ID del Usuario: {cursor.lastrowid + 1}")
    
    borrar_contenido(widgets)
    
def ventana_dialogo(titulo: str, mensaje: str, tipo: QMessageBox.icon):
    mensaje = QMessageBox
    mensaje.setIcon(tipo)
    mensaje.setWindowTitle(titulo)
    mensaje.setText(mensaje)
    mensaje.exec_()