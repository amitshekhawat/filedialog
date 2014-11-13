import sys
from PyQt4 import QtCore, QtGui

from filebrowse import Ui_notepad

class StartQT4(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_notepad()
		self.ui.setupUi(self)
		# tutaj dajemy wlasne polaczenia slotow
		QtCore.QObject.connect(self.ui.button_open,QtCore.SIGNAL("clicked()"), self.file_dialog)
	def file_dialog(self):
		fd = QtGui.QFileDialog(self)
		self.filename = fd.getOpenFileName()
                self.ui.le.setText(self.filename)
		

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartQT4()
	myapp.show()
	sys.exit(app.exec_())
