# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created: Wed May 10 15:31:54 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from os import path
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

class Ui_Dialog(object):
    def resourse_path(self,relative_path):
        if hasattr(sys,"_MEIPASS"):
            base_path = sys._MEIPASS
        else:
            base_path = path.abspath(".")
        return path.join(base_path,relative_path)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(900, 600)
        Form.setSizeGripEnabled(True)

        palett1 = QtGui.QPalette()
        palett1.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap(self.resourse_path('resourse/back_2.jpg'))))
        Form.setAutoFillBackground(True)
        Form.setPalette(palett1)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resourse_path('resourse/z.ico')),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 211, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        #源excel标签
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 450, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        #4
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 500, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        #命令1
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(340, 20, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        #命令1的输入
        self.lineEdit_5 = QtGui.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(400, 20, 211, 21))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit"))
        #命令2
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(340, 70, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_5"))
        #change status
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(750, 70, 110, 22))
        self.label_7.setObjectName(_fromUtf8("label_2"))

        #命令2的输入
        self.lineEdit_6 = QtGui.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(400, 70, 211, 21))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit"))



        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 70, 211, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        #源xcel
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 450, 451, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 500, 451, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        #第一按钮
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(650, 20, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 70, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 450, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        #open telnet
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(750, 20, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))



        self.textBrowser_Back_1 = QtGui.QTextBrowser(Form)
        self.textBrowser_Back_1.setGeometry(QtCore.QRect(20, 120, 360, 300))
        self.textBrowser_Back_1.setObjectName(_fromUtf8("textBrowser_Back"))
        #显示区域2
        self.textBrowser_Back_2 = QtGui.QTextBrowser(Form)
        self.textBrowser_Back_2.setGeometry(QtCore.QRect(400, 120, 360, 300))
        self.textBrowser_Back_2.setObjectName(_fromUtf8("textBrowser_Back_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "我真的只是一个小工具，不要把我送给别人", None))
        self.lineEdit.setText(_translate("Form", "192.168.18.252", None))
        self.label.setText(_translate("Form", "IP 1", None))
        self.label_2.setText(_translate("Form", "IP 2", None))
        self.label_3.setText(_translate("Form", "源excel", None))
        self.label_4.setText(_translate("Form", "目标excel", None))
        self.label_5.setText(_translate("Form", "命令 1", None))
        self.label_6.setText(_translate("Form", "命令 2", None))
        self.label_7.setText(_translate("Form", "欢迎使用！", None))
        #命令1内容
        self.lineEdit_5.setText(_translate("Form", "uptime", None))
        #命令2内容
        self.lineEdit_6.setText(_translate("Form", "ls", None))
        self.lineEdit_2.setText(_translate("Form", "192.168.18.138", None))
        self.lineEdit_3.setText(_translate("Form", "C:\\Users\\Administrator\\Documents\\test\\changqilaohua-input\\new.xls", None))
        self.lineEdit_4.setText(_translate("Form", "C:\\Users\\Administrator\\Documents\\test\\changqilaohua-output", None))
        self.pushButton.setText(_translate("Form", "执行对比", None))
        self.pushButton_2.setText(_translate("Form", "清屏", None))
        self.pushButton_3.setText(_translate("Form", "查老化", None))
        self.pushButton_4.setText(_translate("Form", "开Telnet", None))

