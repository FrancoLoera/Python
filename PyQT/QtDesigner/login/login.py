# Importaciones de PyQt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# Importaciones de funcionalidad
import sys, sqlite3
from sqlite3 import Error
import utilidades

try:
    with sqlite3.connect('login_db.db', detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as conexion:
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        # TABLA USUARIO
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS USUARIO(
                        idUsuario INTEGER,
                        nombreCompleto TEXT NOT NULL,
                        correoElectronico TEXT NOT NULL,
                        contrasena TEXT NOT NULL,
                        CONSTRAINT PK_USUARIO PRIMARY KEY(idUsuario)
                        );
                    """)
        
        # TABLA PROVEEDOR
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS PROVEEDOR(
                        idProveedor INTEGER,
                        razonSocial TEXT NOT NULL,
                        rfc TEXT NOT NULL,
                        correo TEXT NOT NULL,
                        telefono TEXT NOT NULL,
                        idUsuario INTEGER,
                        CONSTRAINT PK_PROVEEDOR PRIMARY KEY(idProveedor),
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
                
                cursor.execute("SELECT * FROM USUARIO WHERE correoElectronico = ? AND contrasena = ?", (input_Correo, input_Password))
                resultado = cursor.fetchone()
                
                utilidades.conexion_LineEdit_PushButton_all([self.lineEdit, self.lineEdit_2], self.pushButton)
                self.panel = Panel(self)
                self.panel.show()
                self.close()
                
                """if resultado:
                    conexion_LineEdit_PushButton_all([self.lineEdit, self.lineEdit_2], self.pushButton)
                    self.panel = Panel(self)
                    self.panel.show()
                    self.close()  # Oculta la ventana de login
                else:
                    QMessageBox.warning(self, "Error", "Correo o contraseña incorrectos")"""

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
                    
        class PanelUsuario(QMainWindow):
            def __init__(self, ventana_Anterior):
                super().__init__()
                
                self.ventana_Anterior = ventana_Anterior
                
                uic.loadUi("panel_usuario.ui", self)
                
                self.setWindowTitle("NeuralCore - Panel de Usuarios")
                self.setWindowIcon(QIcon("favicon.png"))
                self.setWindowOpacity(0.9)
                
                utilidades.centrar_ventana(self)
                
                self.pushButton.clicked.connect(self.regresar)
                self.stackedWidget.setCurrentIndex(0)
                
                utilidades.conexion_LineEdit_PushButton_any([self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4], self.pushButton_6)
                utilidades.conexion_LineEdit_PushButton_all([self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4], self.pushButton_7)
                utilidades.conexion_pushButton_borrado(self.pushButton_6, [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4])
                utilidades.conectar_pushButton_index(self, self.stackedWidget, [self.pushButton_5, self.pushButton_4, self.pushButton_3, self.pushButton_2], conexion)
                
                self.pushButton_7.clicked.connect(lambda: utilidades.agregar_registro(self, self.label_7, [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4], conexion))
                
                self.id_usuarios = []
                # self.tableWidget_2.cellChanged.connect(self.actualizar_usuario)
                self.tableWidget_3.itemSelectionChanged.connect(self.habilitar_boton)
                self.pushButton_9.clicked.connect(self.borrar_usuario)
                
                cursor.execute("SELECT MAX(idUsuario) FROM USUARIO")
                resultado = f"ID del Usuario: {cursor.fetchone()[0] + 1}"
                
                self.label_7.setText(resultado)
                
            def agregar_usuario(self):
                correo = self.lineEdit_2.text()
                cursor.execute("SELECT COUNT(*) FROM USUARIO WHERE correoElectronico = ?", (correo, ))
                resultado = cursor.fetchone()[0]
                
                if resultado:
                    QMessageBox.warning(self, "Error", "Ya existe un usuario con este correo electrónico")
                    
                else:
                    if utilidades.validacion_correo_widget(self, self.lineEdit_2):
                        nombre_Usuario = self.lineEdit.text()
                        contrasena = self.lineEdit_3.text()
                        contrasena_repetida = self.lineEdit_4.text()
                        
                        if contrasena == contrasena_repetida:
                            cursor.execute("INSERT INTO USUARIO(nombreCompleto, correoElectronico, contrasena) VALUES(?, ?, ?)",
                                        (nombre_Usuario, correo, contrasena))
                            conexion.commit()
                            QMessageBox.information(self, "Éxito", "El usuario se ha registrado exitosamente", QMessageBox.Ok)
                            
                            cursor.execute("SELECT MAX(idUsuario) FROM USUARIO")
                            resultado = f"ID del Usuario: {cursor.fetchone()[0] + 1}"
                            
                            self.label_7.setText(resultado)                    
                            
                            self.lineEdit.clear()
                            self.lineEdit_2.clear()
                            self.lineEdit_3.clear()
                            self.lineEdit_4.clear()
                        
                        else:
                            QMessageBox.warning(self, "Contrañenas Distintas", "Las contraseñas no coinciden.")
                        
            """ def actualizar_usuario(self, fila, columna):
                id_usuario = self.id_usuarios[fila]
                nuevo_valor = self.tableWidget_2.item(fila, columna).text()
                columna_nombre = ["nombreCompleto", "correoElectronico", "contrasena"][columna]
                
                if nuevo_valor:
                    if (columna_nombre == "correoElectronico") and (validacion_correo_texto(self, nuevo_valor)):
                        cursor.execute(f"UPDATE USUARIO SET {columna_nombre} = ? WHERE idUsuario = ?", (nuevo_valor, id_usuario))
                        conexion.commit()
                        
                    elif (columna_nombre == "correoElectronico"):
                        self.cargar_datos_CUD(self.tableWidget_2)
                        
                    else:
                        cursor.execute(f"UPDATE USUARIO SET {columna_nombre} = ? WHERE idUsuario = ?", (nuevo_valor, id_usuario))
                        conexion.commit()
                        
                else:
                    QMessageBox.warning(self, "Campo Vacío", "No puede dejar el campo vacío.")
                    self.cargar_datos_CUD(self.tableWidget_2) """
                
            def regresar(self):
                self.ventana_Anterior.show()
                self.close()
                
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
                resultado = f"ID del Producto: {cursor.fetchone()[0] + 1}"
                
                self.label_11.setText(resultado)
                
                validator_int = QIntValidator()
                validator_float = QDoubleValidator()
                
                self.lineEdit_3.setValidator(validator_float)
                self.lineEdit_4.setValidator(validator_int)
                self.lineEdit_5.setValidator(validator_int)
                
                self.stackedWidget.setCurrentIndex(0)
                
                utilidades.conexion_LineEdit_PushButton_any([self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5], self.pushButton_10)
                utilidades.conexion_LineEdit_PushButton_all([self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5], self.pushButton_11)
                utilidades.conexion_pushButton_borrado(self.pushButton_10, [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5])
                utilidades.conectar_pushButton_index(self, self.stackedWidget, [self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9], conexion)
                
                self.pushButton_11.clicked.connect(self.agregar_producto)
                
            def regresar(self):
                self.ventana_anterior.show()
                self.close()
                
            def agregar_producto(self):
                nombre = self.lineEdit.text()
                precio = int(self.lineEdit_3.text())
                inventario = int(self.lineEdit_4.text())
                proveedor = self.lineEdit_5.text()
                
                cursor.execute("SELECT COUNT(*) FROM PRODUCTO WHERE nombre = ? AND idProveedor = ?", (nombre, proveedor))
                
                # Validación producto único
                if cursor.fetchone():
                    QMessageBox.warning(self, "Error", "Este producto ya ha sido registrado previamente.")
                    
                # Validación precio mayor a 0
                elif precio <= 0:
                    QMessageBox.warning(self, "Error", "El precio del producto no puede ser menor a 1.")
                    
                elif inventario <= 0:
                    QMessageBox.warning(self, "Error", "El inventario del producto no puede ser menor a 1.")
                    
                else:
                    if utilidades.consulta_agregar([self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5],
                                    ["nombre", "descripcion", "precio", "inventario", "idProveedor"],
                                    "PRODUCTO", conexion
                                    ):
                        QMessageBox.information(self, "Éxito", "El producto se ha registrado exitosamente.")
        
        if __name__ == "__main__": 
            app = QApplication(sys.argv)
            
            login = MainWindow()
            login.show()
            
            sys.exit(app.exec_())

except Error as e:
    print(f"Se ha presentado un error con el manejador de bases de datos")
    print(f"Tipo de error: {type(e)}")
    print(f"Mensaje del error: {e}")