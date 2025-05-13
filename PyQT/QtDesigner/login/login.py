# Importaciones de PyQt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# Importaciones de funcionalidad
import sys, sqlite3
import utilidades

try:
    with sqlite3.connect("login_db.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conexion:
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        # TABLA USUARIO
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS USUARIO(
                        idUsuario INTEGER,
                        nombreCompleto TEXT NOT NULL,
                        correoElectronico TEXT NOT NULL,
                        contrasena TEXT NOT NULL,
                        CONSTRAINT PK_USUARIO PRIMARY KEY(idUsuario),
                        CONSTRAINT UQ_nombreCompleto_USUARIO UNIQUE(nombreCompleto),
                        CONSTRAINT UQ_correoElectronico_USUARIO UNIQUE(correoElectronico)
                        );
                    """)
        
        # TABLA PROVEEDOR
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS PROVEEDOR(
                        idProveedor INTEGER,
                        nombre TEXT NOT NULL,
                        razonSocial TEXT NOT NULL,
                        rfc TEXT NOT NULL,
                        correoElectronico TEXT NOT NULL,
                        telefono TEXT NOT NULL,
                        idUsuario INTEGER,
                        CONSTRAINT PK_PROVEEDOR PRIMARY KEY(idProveedor),
                        CONSTRAINT UQ_rfc_PROVEEDOR UNIQUE(rfc),
                        CONSTRAINT UQ_correoElectronico_PROVEEDOR UNIQUE(correoElectronico),
                        CONSTRAINT UQ_telefono_PROVEEDOR UNIQUE(telefono),
                        CONSTRAINT FK_idUsuario_USUARIO FOREIGN KEY(idUsuario) REFERENCES USUARIO(idUsuario) ON DELETE CASCADE
                        );
                    """)
        
        # TABLA PRODUCTO
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS PRODUCTO(
                        idProducto INTEGER,
                        nombre TEXT NOT NULL,
                        descripcion TEXT NOT NULL,
                        precio REAL NOT NULL,
                        inventario INTEGER NOT NULL,
                        idProveedor INTEGER NOT NULL,
                        CONSTRAINT PK_PRODUCTO PRIMARY KEY(idProducto),
                        CONSTRAINT UQ_nombre_PRODUCTO UNIQUE(nombre),
                        CONSTRAINT FK_idProveedor_PRODUCTO FOREIGN KEY(idProveedor) REFERENCES PROVEEDOR(idProveedor) ON DELETE CASCADE
                        );
                    """)
        
        class MainWindow(QMainWindow):
            def __init__(self, *args):
                super().__init__()
                
                uic.loadUi("login.ui", self)
                
                self.setWindowTitle("NeuralCore - Login")
                self.setWindowIcon(QIcon("favicon.png"))
                self.setWindowOpacity(0.9)
                
                utilidades.centrar_ventana(self)
                
                self.pushButton_2.setEnabled(False)
                self.pushButton.setEnabled(False)
                
                utilidades.conexion_LineEdit_PushButton_any([self.lineEdit, self.lineEdit_2], self.pushButton_2)
                utilidades.conexion_LineEdit_PushButton_all([self.lineEdit, self.lineEdit_2], self.pushButton)
                
                self.pushButton.clicked.connect(self.verificar_login)
                
                utilidades.conexion_pushButton_borrado(self.pushButton_2, [self.lineEdit, self.lineEdit_2])
                
            def verificar_login(self):
                input_Correo = self.lineEdit_2.text()
                input_Password = self.lineEdit.text()
                
                cursor.execute("SELECT COUNT(*) FROM USUARIO WHERE correoElectronico = ? AND contrasena = ?", (input_Correo, input_Password))
                resultado = cursor.fetchone()[0]
                
                utilidades.conexion_LineEdit_PushButton_all([self.lineEdit, self.lineEdit_2], self.pushButton)
                
                self.panel = Panel(self)
                self.panel.show()
                self.close()  # Oculta la ventana de login
                
                """ if resultado:
                    self.panel = Panel(self)
                    self.panel.show()
                    self.close()  # Oculta la ventana de login
                else:
                    QMessageBox.warning(self, "Error", "Correo o contraseña incorrectos") """

        class Panel(QMainWindow):
            def __init__(self, ventana_Anterior):
                super().__init__()
                
                self.ventana_Anterior = ventana_Anterior
                
                uic.loadUi("panel.ui", self)
                
                self.setWindowIcon(QIcon("favicon.png"))
                self.setWindowOpacity(0.9)
                self.setWindowTitle("NeuralCore - Panel de Administración")
                
                utilidades.centrar_ventana(self)
                
                self.pushButton.clicked.connect(self.regresar)
                self.toolButton_2.clicked.connect(self.panel_Usuario)
                self.toolButton.clicked.connect(self.panel_Producto)
                self.toolButton_3.clicked.connect(self.panel_Proveedor)
                
            def regresar(self):
                self.ventana_Anterior.show()  # Vuelve a mostrar la ventana de login
                self.close()  # Cierra la ventana de panel
                
            def panel_Usuario(self):
                self.panel = PanelUsuario(self)
                self.panel.show()
                self.close()
                
            def panel_Producto(self):
                self.panel = PanelProducto(self)
                self.panel.show()
                self.close()
                
            def panel_Proveedor(self):
                self.panel = PanelProveedor(self)
                self.panel.show()
                self.close()
                    
        class PanelUsuario(QMainWindow):
            def __init__(self, ventana_Anterior):
                super().__init__()
                
                self.ventana_Anterior = ventana_Anterior
                
                uic.loadUi("panel_usuario.ui", self)
                
                self.setWindowTitle("NeuralCore - Panel de Usuarios")
                self.setWindowIcon(QIcon("favicon.png"))
                self.setWindowOpacity(0.9)
                
                utilidades.centrar_ventana(self)
                
                # Bind para botón Regresar
                self.pushButton.clicked.connect(self.regresar)
                
                # Bind para establecer Página 0
                self.stackedWidget.setCurrentIndex(0)
                
                # Bind para evaluar botón Limpiar
                utilidades.conexion_LineEdit_PushButton_any([self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4], self.pushButton_6)
                
                # Bind para evaluar botón Registrar
                utilidades.conexion_LineEdit_PushButton_all([self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4], self.pushButton_7)
                
                # Bind para ejecutar botón Limpiar
                utilidades.conexion_pushButton_borrado(self.pushButton_6, [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4])
                
                # Bind para cambiar de Página
                utilidades.conectar_pushButton_index(self, self.stackedWidget, [self.pushButton_5, self.pushButton_4, self.pushButton_3, self.pushButton_2], conexion)
                
                # Bind para Agregar usuario
                self.pushButton_7.clicked.connect(lambda: utilidades.agregar_registro(self, self.label_7, [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4], conexion))
                
                # Bind para Actualizar usuario
                self.tableWidget_2.cellChanged.connect(self.on_cell_changed)
                self.editando = False
                
                self.tableWidget_3.itemSelectionChanged.connect(self.habilitar_boton)
                self.pushButton_9.clicked.connect(self.borrar_usuario)
                
                cursor.execute("SELECT MAX(idUsuario) FROM USUARIO")
                max = cursor.fetchone()[0]
                
                if max:
                    resultado = f"ID del Usuario: {max + 1}"
                    self.label_7.setText(resultado)
                
                else:
                    self.label_7.setText("ID del Usuario: 1")
                
            def regresar(self):
                self.ventana_Anterior.show()
                self.close()
                
            def on_cell_changed(self, fila, columna):
                if self.editando:
                    return
                utilidades.actualizar_registro(self, self.tableWidget_2, fila, columna, conexion)
                
            def borrar_usuario(self):
                filas_seleccionadas = self.tableWidget_3.selectionModel().selectedRows()
                
                confirmacion = QMessageBox.question(
                    self,
                    "Confirmar Eliminación",
                    f"¿Deseas eliminar {len(filas_seleccionadas)} usuario(s)?",
                    QMessageBox.Yes | QMessageBox.No
                )
                
                if confirmacion == QMessageBox.Yes:
                    ids_borrado = []
                    
                    for fila in filas_seleccionadas:
                        fila = fila.row()
                        id_usuario = self.id_usuarios[fila]
                        ids_borrado.append(id_usuario)
                        
                    for id in ids_borrado:
                        cursor.execute("UPDATE PROVEEDOR SET idUsuario = NULL WHERE idUsuario = ?", (id,))
                        cursor.execute("DELETE FROM USUARIO WHERE idUsuario = ?", (id,))
                        
                    conexion.commit()
                    
                    QMessageBox.information(self, "Éxito", "Usuario(s) eliminado(s) correctamente.")

                    self.cargar_datos_CUD(self.tableWidget_3)
        
            def habilitar_boton(self):
                if self.tableWidget_3.selectedItems():
                    self.pushButton_9.setEnabled(True)
                else:
                    self.pushButton_9.setEnabled(False)
                    
        class PanelProducto(QMainWindow):
            def __init__(self, ventana_anterior):
                super().__init__()
                
                self.ventana_anterior = ventana_anterior
                
                uic.loadUi("panel_producto.ui", self)
                
                self.setWindowTitle("NeuralCore - Panel de Productos")
                self.setWindowIcon(QIcon("favicon.png"))
                self.setWindowOpacity(0.9)
                
                utilidades.centrar_ventana(self)
                
                self.pushButton.clicked.connect(self.regresar)
                
                cursor.execute("SELECT MAX(idProducto) FROM PRODUCTO")
                max = cursor.fetchone()[0]
                
                if max:
                    resultado = f"ID del Producto: {max + 1}"
                    self.label_11.setText(resultado)
                
                else:
                    self.label_11.setText("ID del Producto: 1")
                
                validator_int = QIntValidator()
                validator_float = QDoubleValidator()
                
                self.lineEdit_3.setValidator(validator_float)
                self.lineEdit_4.setValidator(validator_int)
                self.lineEdit_5.setValidator(validator_int)
                
                # Bind para establecer Página 0
                self.stackedWidget.setCurrentIndex(0)
                
                # Bind para evaluar botón Limpiar
                utilidades.conexion_LineEdit_PushButton_any([self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5], self.pushButton_10)
                
                # Bind para evaluar botón Registrar
                utilidades.conexion_LineEdit_PushButton_all([self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5], self.pushButton_11)
                
                # Bind para ejecutar botón Limpiar
                utilidades.conexion_pushButton_borrado(self.pushButton_10, [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5])
                
                # Bind para cambiar de Página
                utilidades.conectar_pushButton_index(self, self.stackedWidget, [self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9], conexion)
                
                # Bind para Agregar producto
                self.pushButton_11.clicked.connect(lambda: utilidades.agregar_registro(self, self.label_11, [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5], conexion))
                
                # Bind para Actualizar producto
                self.tableWidget_2.cellChanged.connect(self.on_cell_changed)
                self.editando = False
                
            def regresar(self):
                self.ventana_anterior.show()
                self.close()
            
            def on_cell_changed(self, fila, columna):
                if self.editando:
                    return
                utilidades.actualizar_registro(self, self.tableWidget_2, fila, columna, conexion)
                
        class PanelProveedor(QMainWindow):
            def __init__(self, ventana_Anterior):
                super().__init__()
                
                self.ventana_Anterior = ventana_Anterior
                
                uic.loadUi("panel_proveedor.ui", self)
                
                self.setWindowTitle("NeuralCore - Panel de Proveedores")
                self.setWindowIcon(QIcon("favicon.png"))
                self.setWindowOpacity(0.9)
                
                utilidades.centrar_ventana(self)
                
                # Bind para botón Regresar
                self.pushButton_2.clicked.connect(self.regresar)
                
                cursor.execute("SELECT MAX(idProveedor) FROM PROVEEDOR")
                max = cursor.fetchone()[0]
                
                if max:
                    resultado = f"ID del Proveedor: {max + 1}"
                    self.label_20.setText(resultado)
                
                else:
                    self.label_20.setText("ID del Proveedor: 1")
                
                validator_int = QIntValidator()
                self.lineEdit_8.setValidator(validator_int)
                
                # Bind para establecer Página 0
                self.stackedWidget_2.setCurrentIndex(0)
                
                # Bind para evaluar botón Limpiar
                utilidades.conexion_LineEdit_PushButton_any([self.radioButton, self.radioButton_2, self.lineEdit, self.lineEdit_6, self.lineEdit_7, self.lineEdit_8], self.pushButton_17)
                
                # Bind para evaluar botón Registrar
                utilidades.conexion_LineEdit_PushButton_all([self.radioButton, self.radioButton_2, self.lineEdit, self.lineEdit_6, self.lineEdit_7, self.lineEdit_8], self.pushButton_18)
                
                # Bind para ejecutar botón Limpiar
                utilidades.conexion_pushButton_borrado(self.pushButton_17, [self.radioButton, self.radioButton_2, self.lineEdit, self.lineEdit_6, self.lineEdit_7, self.lineEdit_8])
                
                # Bind para cambiar de Página
                utilidades.conectar_pushButton_index(self, self.stackedWidget_2, [self.pushButton_13, self.pushButton_14, self.pushButton_15, self.pushButton_16], conexion)
                
                # Bind para Agregar proveedor
                self.pushButton_18.clicked.connect(lambda: utilidades.agregar_registro(self, self.label_20, [self.lineEdit, self.radioButton, self.radioButton_2, self.lineEdit_6, self.lineEdit_7, self.lineEdit_8], conexion))
                
                # Bind para Actualizar producto
                self.tableWidget_2.cellChanged.connect(self.on_cell_changed)
                self.editando = False
                
            def regresar(self):
                self.ventana_Anterior.show()
                self.close()
                
            def on_cell_changed(self, fila, columna):
                if self.editando:
                    return
                utilidades.actualizar_registro(self, self.tableWidget_2, fila, columna, conexion)
        
        if __name__ == "__main__": 
            app = QApplication(sys.argv)
            
            login = MainWindow()
            login.show()
            
            sys.exit(app.exec_())

except Exception:
    excepcion = sys.exc_info()
    print(f"Se ha presentado un error con el manejador de bases de datos")
    print(f"Tipo de error: {excepcion[0]}")
    print(f"Mensaje del error: {excepcion[1]}")