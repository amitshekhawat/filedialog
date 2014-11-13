# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filebrowse.ui'
#
# Created: Thu Nov 13 20:23:52 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_notepad(object):
    def setupUi(self, notepad):
        notepad.setObjectName(_fromUtf8("notepad"))
        notepad.resize(469, 465)
        self.centralwidget = QtGui.QWidget(notepad)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.le = QtGui.QLineEdit(self.centralwidget)
        self.le.setGeometry(QtCore.QRect(0, 170, 221, 27))
        self.le.setObjectName(_fromUtf8("le"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 170, 71, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.button_open = QtGui.QPushButton(self.centralwidget)
        self.button_open.setGeometry(QtCore.QRect(220, 170, 98, 27))
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 381, 111))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        notepad.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(notepad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 469, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        notepad.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(notepad)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        notepad.setStatusBar(self.statusbar)

        self.retranslateUi(notepad)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), notepad.close)
        QtCore.QMetaObject.connectSlotsByName(notepad)

    def retranslateUi(self, notepad):
        notepad.setWindowTitle(_translate("notepad", "MainWindow", None))
        self.pushButton.setText(_translate("notepad", "Close", None))
        self.button_open.setText(_translate("notepad", "Open File", None))

