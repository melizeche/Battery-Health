#!/usr/bin/python
#Autor: Marcelo Elizeche
#Liberado bajo licencia GPLv3

import sys,string
from PyQt4 import QtCore, QtGui, QtNetwork
from ui import Ui_Dialog

global info

class StartGUI(QtGui.QDialog):
	def __init__(self, parent=None):
		global info
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)	
		self.leerInfo()
		self.displayInfo()
		
	def leerInfo(self):
		global info
		f= open("/proc/acpi/battery/BAT0/info") #obtenemos la informacion de /proc
		text=f.readlines()
	#	print text
		present = text[0].split(':')[1].strip() #Checkeamos si hay bateria o no 
		if(present=='no'):
			info = (present,'','')
			return 0
		else:
			
		#	print present
			maxcap = text[1].split(':')[1].strip().split(' ')[0] #parseamos la capacidad maxima de bateria
		#	print maxcap
			maxfull = text[2].split(':')[1].strip().split(' ')[0] #parseamos la capacidad maxima de la ultima carga
			#maxfull=int(maxfull)
		#	print maxfull
			f.close()
			info = (present,maxcap,maxfull)
			return 1
		
	def displayInfo(self):
		global info
		#print info
		if(info[0]=='yes'): #cargamos la informacion en los widgets
			self.ui.lineEdit.setText(info[1] + ' mWh')  
			self.ui.lineEdit_2.setText(info[2] + ' mWh') 
			batHealth = (int(info[2])*100)/int(info[1]) # "Calculo" del porcentaje de 'Salud' de la bateria
			self.ui.progressBar.setProperty("value", batHealth)
			self.ui.label_3.setText(str(self.ui.label_3.text()) + str(100-batHealth) + ' %')
			#self.ui.lineEdit_3.setText(str(batHealth) + ' %')
		else:
			self.ui.lineEdit.setText("NO BAT")
		

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartGUI()
	
	myapp.show()
	sys.exit(app.exec_())
