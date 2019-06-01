# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from cgitb import text
from PyQt5.Qt import QMessageBox

class Ui_Form(object):
    
    fac_list=[]
    ins_list=[]
    edges=[]
    
    def answer_add_click1(self):
        text=self.lineEdit.text()
        text=text.split()
        text=text.lower()
        if text not in self.fac_list or text != '':
            self.fac_list.append(text)
            self.listWidget.addItem(text)
        
        elif text=="":
            message=QtWidgets.QMessageBox()
            message.setText("line edit is empty")
            message.setStandardButtons(QMessageBox.Ok)
            message.show()
            message.buttonClicked.connect(message.close)
        else:
            message=QtWidgets.QMessageBox()
            message.setText("this node added before")
            message.setStandardButtons(QMessageBox.Ok)
            message.show()
            message.buttonClicked.connect(message.close)
    
    def answer_add_click2(self):
        text=self.lineEdit_2.text()
        text=text.split()
        text=text.lower()
        if text not in self.ins_list or text != '' or text not in self.fac_list:
            self.ins_list.append(text)
            self.listWidget_2.addItem(text)
        
        elif text=="":
            message=QtWidgets.QMessageBox()
            message.setText("line edit is empty")
            message.setStandardButtons(QMessageBox.Ok)
            message.show()
            message.buttonClicked.connect(message.close)
        else:
            message=QtWidgets.QMessageBox()
            message.setText("this node added before")
            message.setStandardButtons(QMessageBox.Ok)
            message.show()
            message.buttonClicked.connect(message.close)
        
    def answer_next_click1(self):
        if self.listWidget.count() == 0:
            message=QtWidgets.QMessageBox()
            message.setText("the list of nodes is empty")
            message.setStandardButtons(QMessageBox.Ok)
            message.show()
            message.buttonClicked.connect(message.close)
        else:
            self.stackedWidget.setCurrentIndex(1)
            
    def answer_next_click2(self):
        if self.listWidget_2.count() == 0:
            message=QtWidgets.QMessageBox()
            message.setText("the list of nodes is empty")
            message.setStandardButtons(QMessageBox.Ok)
            message.show()
            message.buttonClicked.connect(message.close)
        else:
            self.stackedWidget.setCurrentIndex(2)
            list_alaki=[]
            for i in range(0,(len(self.fac_list)+len(self.ins_list)-1)):
                list_alaki.append(0)
                
            for i in range(0,(len(self.fac_list)+len(self.ins_list)-1)):
                self.edges.append(list_alaki)
                
    def answer_add_edges(self):
        row=self.listWidget_3.currentRow()
        column=self.listWidget_4.currentRow()
        if self.listWidget_3.currentRow()!= -1 and self.listWidget_4.currentRow() != -1 and self.lineEdit_3.text().split() != '':
            txt=self.lineEdit_3.text().split()
            try:
                txt=int(txt)
                self.edges[row][column]=text
            except TypeError:
                message=QtWidgets.QMessageBox()
                message.setText("distance must be number")
                message.setStandardButtons(QMessageBox.Ok)
                message.show()
                message.buttonClicked.connect(message.close)
        else:
            message=QtWidgets.QMessageBox()
            message.setText("you should select two different nodes and write the distance of between them")
            message.setStandardButtons(QMessageBox.Ok)
            message.show()
            message.buttonClicked.connect(message.close)
            
    def answer_next_click3(self):
        message=QtWidgets.QMessageBox()
        message.setText("the data is saved")
        message.setStandardButtons(QMessageBox.Ok)
        message.show()
        message.buttonClicked.connect(message.close)
        self.stackedWidget.setCurrentIndex(3)
            
            
            
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(592, 389)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 601, 391))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(90, 0, 511, 391))
        self.label.setStyleSheet("background-image: url(./background/background1.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(36, 30, 91, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(450, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(155, 100, 271, 231))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(160, 80, 261, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 340, 271, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(90, 0, 511, 391))
        self.label_4.setStyleSheet("background-image: url(./background/background1.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 30, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 30, 281, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(26, 30, 111, 20))
        self.label_5.setObjectName("label_5")
        self.listWidget_2 = QtWidgets.QListWidget(self.page_3)
        self.listWidget_2.setGeometry(QtCore.QRect(150, 100, 271, 231))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(160, 80, 251, 20))
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 340, 271, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        self.label_7.setGeometry(QtCore.QRect(80, 0, 521, 391))
        self.label_7.setStyleSheet("background-image: url(./background/background1.jpg);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.listWidget_3 = QtWidgets.QListWidget(self.page_4)
        self.listWidget_3.setGeometry(QtCore.QRect(20, 70, 181, 261))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 171, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_4)
        self.label_9.setGeometry(QtCore.QRect(230, 150, 131, 31))
        self.label_9.setObjectName("label_9")
        self.listWidget_4 = QtWidgets.QListWidget(self.page_4)
        self.listWidget_4.setGeometry(QtCore.QRect(370, 70, 181, 261))
        self.listWidget_4.setObjectName("listWidget_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 220, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(220, 220, 47, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(340, 220, 21, 16))
        self.label_11.setObjectName("label_11")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 260, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_6.setGeometry(QtCore.QRect(174, 340, 241, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setGeometry(QtCore.QRect(370, 30, 141, 20))
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_13 = QtWidgets.QLabel(self.page_5)
        self.label_13.setGeometry(QtCore.QRect(6, 2, 581, 351))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_7.setGeometry(QtCore.QRect(14, 360, 571, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.load_label = QtWidgets.QLabel(self.page_2)
        self.load_label.setGeometry(QtCore.QRect(0, 2, 591, 381))
        self.load_label.setText("")
        self.load_label.setObjectName("load_label")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex()
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pushButton.clicked.connect(self.answer_add_click1)
        self.pushButton_2.clicked.connect(self.answer_next_click1)
        self.pushButton_3.clicked.connect(self.answer_add_click2)
        self.pushButton_4.clicked.connect(self.answer_next_click2)
        self.pushButton_5.clicked.connect(self.answer_add_edges)
        self.pushButton_6.clicked.connect()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "name of factory :"))
        self.pushButton.setText(_translate("Form", "add"))
        self.label_3.setText(_translate("Form", "list of factories"))
        self.pushButton_2.setText(_translate("Form", "next"))
        self.pushButton_3.setText(_translate("Form", "add"))
        self.label_5.setText(_translate("Form", "name of instersection"))
        self.label_6.setText(_translate("Form", "list of instersections"))
        self.pushButton_4.setText(_translate("Form", "next"))
        self.label_8.setText(_translate("Form", "choose the one of nodes"))
        self.label_9.setText(_translate("Form", "this place is connected to:"))
        self.label_10.setText(_translate("Form", "distance"))
        self.label_11.setText(_translate("Form", "km"))
        self.pushButton_5.setText(_translate("Form", "add"))
        self.pushButton_6.setText(_translate("Form", "next"))
        self.label_12.setText(_translate("Form", "choose the one of nodes"))
        self.pushButton_7.setText(_translate("Form", "ok"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())

