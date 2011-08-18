#!/usr/bin/python

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
		
		
		#QtCore.QObject.connect(self.ui.searchButton, QtCore.SIGNAL("clicked()"), self.buscar)
		
		self.leerInfo()
		#print 	
		#if
		self.displayInfo()
		
	def leerInfo(self):
		global info
		#print "Hola"
		
		f= open("/proc/acpi/battery/BAT0/info")
		text=f.readlines()
	#	print text
		present = text[0].split(':')[1].strip()
		if(present=='no'):
			info = (present,'','')
			return 0
		else:
			
		#	print present
			maxcap = text[1].split(':')[1].strip().split(' ')[0]
		#	print maxcap
			maxfull = text[2].split(':')[1].strip().split(' ')[0]
			#maxfull=int(maxfull)
		#	print maxfull
			f.close()
			info = (present,maxcap,maxfull)
			return 1
			#f= open("/proc/acpi/battery/BAT0/state")
			#text=f.readlines()
		
	def displayInfo(self):
		global info
		#print info
		if(info[0]=='yes'):
			self.ui.lineEdit.setText(info[1] + ' mWh')  
			self.ui.lineEdit_2.setText(info[2] + ' mWh') 
			#info[2]=int(info[2])
			#info[1]=int(info[1])
			batHealth = (int(info[2])*100)/int(info[1])
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
