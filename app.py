# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import data_base
#from test.test_set import faces
from numpy.lib.function_base import insert
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.Qt import QMessageBox

class Ui_Form(object):
    
    data=data_base.dataBase()
    fac_list=[]
    ins_list=[]
    edges=[]


    def money_button(self):
        self.stackedWidget.setCurrentIndex(7)

    def ok_budget(self):
        self.stackedWidget.setCurrentIndex(8)

    
    def anwer_sale_button(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def anwer_fact_button(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def back_click(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def change_make_address(self):
        self.stackedWidget.setCurrentIndex(3)
        
    def answer_add_click1(self):
        text=self.lineEdit.text()
        text1=text.split()
        text=text.lower()
        if text not in self.fac_list and len(text1)!=0:
            self.fac_list.append(text)
            self.listWidget.addItem(text)
         
        elif text=="":
            self.message.setText("line edit is empty")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
        else:
            self.message.setText("this node added before")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
            
        self.lineEdit.clear()
    
    def answer_add_click2(self):
        text=self.lineEdit_2.text()
        text1=text.split()
        text=text.lower()
        if text not in self.ins_list and len(text1)!=0:
            self.ins_list.append(text)
            self.listWidget_3.addItem(text)

        
        elif text=="":
            self.message.setText("line edit is empty")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
        else:
            self.message.setText("this node added before")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
            
        self.lineEdit_2.clear()
        
    def answer_next_click1(self):
        if self.listWidget.count() == 0:
            self.message.setText("the list of nodes is empty")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
        else:
            self.stackedWidget.setCurrentIndex(4)
            self.listWidget.clear()
            
    def answer_next_click2(self):
        if self.listWidget_3.count() == 0:
            self.message.setText("the list of nodes is empty")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
        else:
            self.stackedWidget.setCurrentIndex(5)
            self.listWidget_3.clear()
            list_alaki=[]
            for i in range(0,(len(self.fac_list)+len(self.ins_list)-1)):
                list_alaki.append(0)
                
            for i in range(0,(len(self.fac_list)+len(self.ins_list)-1)):
                self.edges.append(list_alaki)
                
            for each in self.ins_list:
                self.listWidget_4.addItem(str(each))
                self.listWidget_5.addItem(str(each))
            for each in self.fac_list:
                self.listWidget_4.addItem(str(each))
                self.listWidget_5.addItem(str(each))
                
    def answer_add_edges(self):
        row=self.listWidget_4.currentRow()
        column=self.listWidget_5.currentRow()
        if self.listWidget_4.currentRow()!= -1 and self.listWidget_5.currentRow() != -1 and self.lineEdit_3.text().split() != '':
            txt=self.lineEdit_3.text()
            try:
                txt=int(txt)
                if txt != 0:
                    self.edges[row][column]=txt
                else:
                    self.message.setText("distance cant be 0")
                    self.message.setStandardButtons(QMessageBox.Ok)
                    self.message.show()
                    self.message.buttonClicked.connect(self.message.close)
                    self.lineEdit_3.clear()
            except TypeError:
                self.message.setText("distance must be number")
                self.message.setStandardButtons(QMessageBox.Ok)
                self.message.show()
                self.message.buttonClicked.connect(self.message.close)
                self.lineEdit_3.clear()
        else:
            self.message.setText("you should select two different nodes and write the distance of between them")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
            
    def answer_next_click3(self):
        self.message.setText("the data is saved")
        self.message.setStandardButtons(QMessageBox.Ok)
        self.message.show()
        self.message.buttonClicked.connect(self.message.close)

        self.stackedWidget.setCurrentIndex(6)
        self.listWidget_4.clear()
        self.listWidget_5.clear()
        
        self.data.factory_func.address.fac_nodes=self.fac_list
        self.data.factory_func.address.inst_nodes=self.ins_list
        self.data.factory_func.address.edges=self.edges
        edges_list=self.data.factory_func.address.edgets_list()
        nodes=self.data.factory_func.address.fac_nodes+self.data.factory_func.address.inst_nodes
        G=nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges_list)
         
        color=[]
        for i in range(0,len(self.data.factory_func.address.fac_nodes)):
            color.append('red')
        for i in range(0,len(self.data.factory_func.address.inst_nodes)):
            color.append('blue')
         
        nx.draw_circular(G,node_color = color,with_labels=True,node_size=1000,alpha=1)
        plt.savefig("./Graph.png", format="PNG")
        self.img=QtGui.QImage("./Graph.png")
        self.pic=QtGui.QPixmap.fromImage(self.img)
        self.pixmap5 = self.pic.scaled(self.label_16.width(), self.label_16.height())
        self.label_16.setPixmap(self.pixmap5)

    def answer_ok_click(self):
        self.stackedWidget.setCurrentIndex(1)
  
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 451)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 781, 451))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(270, 0, 541, 481))
        self.label.setStyleSheet("background-image: url(./background/background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(self.page)
        self.toolButton.setGeometry(QtCore.QRect(150, 80, 121, 41))
        self.toolButton.setStyleSheet("background-color: rgb(200, 66, 16);")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.page)
        self.toolButton_2.setGeometry(QtCore.QRect(70, 250, 121, 41))
        self.toolButton_2.setStyleSheet("background-color: rgb(200, 66, 16);")
        self.toolButton_2.setObjectName("toolButton_2")
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_3 = QtWidgets.QLabel(self.page_4)
        self.label_3.setGeometry(QtCore.QRect(270, 0, 511, 451))
        self.label_3.setStyleSheet("background-image: url(./background/background.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.toolButton_8 = QtWidgets.QToolButton(self.page_4)
        self.toolButton_8.setGeometry(QtCore.QRect(100, 170, 131, 41))
        self.toolButton_8.setStyleSheet("background-color: rgb(200, 66, 16);")
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_9 = QtWidgets.QToolButton(self.page_4)
        self.toolButton_9.setGeometry(QtCore.QRect(150, 70, 131, 41))
        self.toolButton_9.setStyleSheet("background-color: rgb(200, 66, 16);")
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_7 = QtWidgets.QToolButton(self.page_4)
        self.toolButton_7.setGeometry(QtCore.QRect(10, 420, 25, 19))
        self.toolButton_7.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons8-back-button-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_10 = QtWidgets.QToolButton(self.page_4)
        self.toolButton_10.setGeometry(QtCore.QRect(50, 290, 131, 41))
        self.toolButton_10.setStyleSheet("background-color: rgb(200, 66, 16);")
        self.toolButton_10.setObjectName("toolButton_10")
        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(270, 0, 511, 451))
        self.label_2.setStyleSheet("background-image: url(./background/background.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_3.setGeometry(QtCore.QRect(150, 30, 131, 41))
        self.toolButton_3.setStyleSheet("background-color: rgb(200, 66, 16);")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_4.setGeometry(QtCore.QRect(90, 330, 141, 41))
        self.toolButton_4.setStyleSheet("background-color: rgb(200, 66, 16);")
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_5.setGeometry(QtCore.QRect(40, 220, 131, 41))
        self.toolButton_5.setStyleSheet("background-color: rgb(200, 66, 16);")
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_6.setGeometry(QtCore.QRect(70, 120, 141, 41))
        self.toolButton_6.setStyleSheet("background-color: rgb(200, 66, 16);")
        self.toolButton_6.setObjectName("toolButton_6")
        self.back = QtWidgets.QToolButton(self.page_3)
        self.back.setGeometry(QtCore.QRect(0, 420, 25, 19))
        self.back.setText("")
        self.back.setIcon(icon)
        self.back.setIconSize(QtCore.QSize(20, 20))
        self.back.setObjectName("back")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(270, 0, 511, 451))
        self.label_4.setStyleSheet("background-image: url(./background/background1.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(110, 30, 91, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit.setGeometry(QtCore.QRect(210, 30, 311, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(540, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(310, 70, 261, 20))
        self.label_6.setObjectName("label_6")
        self.listWidget = QtWidgets.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(220, 100, 271, 271))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 390, 271, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_7 = QtWidgets.QLabel(self.page_5)
        self.label_7.setGeometry(QtCore.QRect(270, 0, 511, 451))
        self.label_7.setStyleSheet("background-image: url(./background/background1.jpg);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_5)
        self.label_8.setGeometry(QtCore.QRect(80, 30, 111, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 30, 311, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 30, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(self.page_5)
        self.label_9.setGeometry(QtCore.QRect(300, 70, 251, 20))
        self.label_9.setObjectName("label_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 390, 261, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget_3 = QtWidgets.QListWidget(self.page_5)
        self.listWidget_3.setGeometry(QtCore.QRect(230, 100, 271, 271))
        self.listWidget_3.setObjectName("listWidget_3")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_10 = QtWidgets.QLabel(self.page_6)
        self.label_10.setGeometry(QtCore.QRect(270, 0, 511, 451))
        self.label_10.setStyleSheet("background-image: url(./background/background1.jpg);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_6)
        self.label_11.setGeometry(QtCore.QRect(80, 50, 171, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_6)
        self.label_12.setGeometry(QtCore.QRect(490, 50, 141, 20))
        self.label_12.setObjectName("label_12")
        self.listWidget_4 = QtWidgets.QListWidget(self.page_6)
        self.listWidget_4.setGeometry(QtCore.QRect(70, 90, 191, 271))
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_5 = QtWidgets.QListWidget(self.page_6)
        self.listWidget_5.setGeometry(QtCore.QRect(480, 90, 191, 271))
        self.listWidget_5.setObjectName("listWidget_5")
        self.label_13 = QtWidgets.QLabel(self.page_6)
        self.label_13.setGeometry(QtCore.QRect(310, 140, 131, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_6)
        self.label_14.setGeometry(QtCore.QRect(280, 200, 47, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 200, 81, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_15 = QtWidgets.QLabel(self.page_6)
        self.label_15.setGeometry(QtCore.QRect(430, 200, 21, 16))
        self.label_15.setObjectName("label_15")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 260, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 390, 241, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.label_16 = QtWidgets.QLabel(self.page_7)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 751, 391))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_7.setGeometry(QtCore.QRect(200, 420, 361, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.stackedWidget.addWidget(self.page_7)

        #ezafe shode
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_17 = QtWidgets.QLabel(self.page_8)
        self.label_17.setGeometry(QtCore.QRect(80, 60, 171, 41))
        self.label_17.setObjectName("label_17")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_8)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 70, 211, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 150, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_18 = QtWidgets.QLabel(self.page_9)
        self.label_18.setGeometry(QtCore.QRect(140, 20, 521, 231))
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_9.setGeometry(QtCore.QRect(350, 360, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.stackedWidget.addWidget(self.page_9)

        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_19 = QtWidgets.QLabel(self.page_10)
        self.label_19.setGeometry(QtCore.QRect(20, 50, 201, 21))
        self.label_19.setObjectName("label_19")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_10)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 50, 531, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_10.setGeometry(QtCore.QRect(430, 120, 93, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_20 = QtWidgets.QLabel(self.page_10)
        self.label_20.setGeometry(QtCore.QRect(170, 340, 461, 61))
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_25 = QtWidgets.QLabel(self.page_10)
        self.label_25.setGeometry(QtCore.QRect(20, 180, 231, 41))
        self.label_25.setObjectName("label_25")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_10)
        self.lineEdit_8.setGeometry(QtCore.QRect(270, 190, 491, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_14.setGeometry(QtCore.QRect(430, 270, 93, 28))
        self.pushButton_14.setObjectName("pushButton_14")
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.label_21 = QtWidgets.QLabel(self.page_11)
        self.label_21.setGeometry(QtCore.QRect(150, 60, 441, 231))
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page_11)
        self.label_22.setGeometry(QtCore.QRect(160, 340, 221, 21))
        self.label_22.setObjectName("label_22")
        self.pushButton_11 = QtWidgets.QPushButton(self.page_11)
        self.pushButton_11.setGeometry(QtCore.QRect(400, 340, 93, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.page_11)
        self.pushButton_12.setGeometry(QtCore.QRect(510, 340, 93, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.label_23 = QtWidgets.QLabel(self.page_12)
        self.label_23.setGeometry(QtCore.QRect(100, 70, 101, 21))
        self.label_23.setObjectName("label_23")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_12)
        self.lineEdit_6.setGeometry(QtCore.QRect(250, 70, 341, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_24 = QtWidgets.QLabel(self.page_12)
        self.label_24.setGeometry(QtCore.QRect(100, 240, 111, 31))
        self.label_24.setObjectName("label_24")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_12)
        self.lineEdit_7.setGeometry(QtCore.QRect(250, 230, 341, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_12)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 340, 93, 28))
        self.pushButton_13.setObjectName("pushButton_13")
        self.stackedWidget.addWidget(self.page_12)


        self.message=QtWidgets.QMessageBox()

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #main page
        self.toolButton.clicked.connect(self.anwer_sale_button)
        self.toolButton_2.clicked.connect(self.anwer_fact_button)
        self.back.clicked.connect(self.back_click)
        self.toolButton_7.clicked.connect(self.back_click)
        self.toolButton_3.clicked.connect(self.change_make_address)
        #add_address
        self.pushButton.clicked.connect(self.answer_add_click1)
        self.pushButton_2.clicked.connect(self.answer_next_click1)
        self.pushButton_3.clicked.connect(self.answer_add_click2)
        self.pushButton_4.clicked.connect(self.answer_next_click2)
        self.pushButton_5.clicked.connect(self.answer_add_edges)
        self.pushButton_6.clicked.connect(self.answer_next_click3)
        self.pushButton_7.clicked.connect(self.answer_ok_click)

        #ezafe shode
        self.toolButton_9.clicked.connect(self.money_button)
        self.pushButton_8.clicked.connect(self.ok_budget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "sale services"))
        self.toolButton_2.setText(_translate("Form", "save  data"))
        self.toolButton_8.setText(_translate("Form", "patten"))
        self.toolButton_9.setText(_translate("Form", "moeny"))
        self.toolButton_10.setText(_translate("Form", "find nearest factory"))
        self.toolButton_3.setText(_translate("Form", "change or make address"))
        self.toolButton_4.setText(_translate("Form", "delete or edit"))
        self.toolButton_5.setText(_translate("Form", "design pattern of carprt"))
        self.toolButton_6.setText(_translate("Form", "change pattern of carpets"))
        self.label_5.setText(_translate("Form", "name of factory :"))
        self.pushButton.setText(_translate("Form", "add"))
        self.label_6.setText(_translate("Form", "list of factories"))
        self.pushButton_2.setText(_translate("Form", "next"))
        self.label_8.setText(_translate("Form", "name of instersection"))
        self.pushButton_3.setText(_translate("Form", "add"))
        self.label_9.setText(_translate("Form", "list of instersections"))
        self.pushButton_4.setText(_translate("Form", "next"))
        self.label_11.setText(_translate("Form", "choose the one of nodes"))
        self.label_12.setText(_translate("Form", "choose the one of nodes"))
        self.label_13.setText(_translate("Form", "this place is connected to:"))
        self.label_14.setText(_translate("Form", "distance"))
        self.label_15.setText(_translate("Form", "km"))
        self.pushButton_5.setText(_translate("Form", "add"))
        self.pushButton_6.setText(_translate("Form", "next"))
        self.pushButton_7.setText(_translate("Form", "ok"))
        self.label_17.setText(_translate("Form", " Please enter your budget:"))
        self.pushButton_8.setText(_translate("Form", "ok"))
        self.pushButton_9.setText(_translate("Form", "ok"))
        self.label_19.setText(_translate("Form", " please enter address of image1:"))
        self.pushButton_10.setText(_translate("Form", "ok"))
        self.label_25.setText(_translate("Form", "  enter address of an image from stock:"))
        self.pushButton_14.setText(_translate("Form", "ok"))
        self.label_22.setText(_translate("Form", "  Do you want to save this image?"))
        self.pushButton_11.setText(_translate("Form", "YES"))
        self.pushButton_12.setText(_translate("Form", "NO"))
        self.label_23.setText(_translate("Form", " Enter name:"))
        self.label_24.setText(_translate("Form", " Enter price:"))
        self.pushButton_13.setText(_translate("Form", "ok"))



if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)

