# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 314)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 110, 231, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(QtGui.QFont("Adobe Heiti Std", 18))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "学号："))
        self.label_2.setText(_translate("Form", "删除学生"))
        self.pushButton.setText(_translate("Form", "删除"))
        self.pushButton_2.setText(_translate("Form", "返回"))
