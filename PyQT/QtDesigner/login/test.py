import sys
import mysql.connector
from mysql.connector import Error

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexión exitosa")
        self.setGeometry(100, 100, 300, 200)
        label = QLabel("Base de datos creada o ya existente.", self)
        label.move(40, 80)

def conectar_mysql():
    print("Conectando desde el hilo principal...")
    try:
        config = {
            "host": "localhost",
            "user": "root",
            "password": "admin"
        }
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            print("Conexión exitosa desde el hilo principal.")
            cursor = conexion.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS ejemplo_db")
            print("Base de datos 'ejemplo_db' creada o ya existente.")
            return True
    except Error as e:
        print(f"Error: {e}")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")
    return False

if __name__ == "__main__":
    if conectar_mysql():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    else:
        print("No se pudo conectar a la base de datos.")
