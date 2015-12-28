#!/usr/bin/env python
# ============= #
# -- IMPORTS -- #
# ============= #

from PyQt5 import QtCore, QtGui, QtWidgets # QtWidgets replaces QtGui in most instances from PyQt4 -> PyQt5
from sys import argv
import os

import display
_translate = QtCore.QCoreApplication.translate # N: Make this a common command

class Engine(QtWidgets.QMainWindow, display.Ui_MainWindow):
	def __init__(self):
		super(Engine, self).__init__()
		self.setupUi(self)
		self.pushButton_NewGame.clicked.connect(self.Thing) #self.object.signal.connect(method)

	def Thing(self):
		self.plainTextEdit_Main.setPlainText(_translate("MainWindow", "Mustafa", None))

# ========================= #
# ------ INITIALIZER ------ #
# ========================= #
# This is the final 

def ParseInput(uinput):
	return "Different!"

def main():
	PHOR = QtWidgets.QApplication(argv)
	CYS = Engine()
	CYS.show()
	PHOR.exec_()

if __name__ == '__main__':
	main()
