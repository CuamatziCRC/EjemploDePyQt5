import sysconfig
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

#Clase heredad de QMainWindow(Constructor de ventanas)
class Ventana(QMainWindow):
	#Metodo Contructor de la clase
	def __init__(self):
		#Iniciar el objeto QMainWindow
		QMainWindow.__init__(self)
		#Cargar la configuracion del archivo .ui en el objeto
		uic.loadUi("MainWindow.ui",self)
		self.setWindowTitle("Cambio de titulo")

#Instancia para iniciar una aplicacion
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostrar la ventana
_ventana.show()
#Ejecutar la aplicacion
app.exec_()		
