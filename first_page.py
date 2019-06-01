# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_page.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import data_base
import add_address

class Ui_Form(object):
    #
    data=data_base.dataBase()
    
    
    #slots
    def anwer_sale_button(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def anwer_fact_button(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def back_click(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def change_make_address(self):
        address_page = QtWidgets.QWidget()
        ui_address = add_address.Ui_Form()
        ui_address.setupUi(address_page)
        address_page.show()
        ui_address.sent_data.connect(self.get_address_data)
        
    @pyqtSlot(list,list,list)    
    def get_address_data(self,fac,ins,edge):
        self.data.factory_func.address.fac_nodes=fac
        self.data.factory_func.address.inst_nodes=ins
        self.data.factory_func.address.edges=edge
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
#         img=QtGui.QImage("./Graph.png")
#         pic=QtGui.QPixmap.fromImage(img)
#         pixmap5 = pic.scaled(self.label.width(), self.label.height())
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 451)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 771, 451))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(260, 0, 541, 481))
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
        self.label_3.setGeometry(QtCore.QRect(260, 0, 511, 451))
        self.label_3.setStyleSheet("background-image: url(./background/background.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.toolButton_8 = QtWidgets.QToolButton(self.page_4)
        self.toolButton_8.setGeometry(QtCore.QRect(60, 260, 131, 41))
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
        icon.addPixmap(QtGui.QPixmap("icons8-back-button-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_7.setObjectName("toolButton_7")
        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(260, 0, 511, 451))
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

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.toolButton.clicked.connect(self.anwer_sale_button)
        self.toolButton_2.clicked.connect(self.anwer_fact_button)
        self.back.clicked.connect(self.back_click)
        self.toolButton_7.clicked.connect(self.back_click)
        self.toolButton_3.clicked.connect(self.change_make_address)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "sale services"))
        self.toolButton_2.setText(_translate("Form", "save  data"))
        self.toolButton_8.setText(_translate("Form", "patten"))
        self.toolButton_9.setText(_translate("Form", "moeny"))
        self.toolButton_3.setText(_translate("Form", "change or make address"))
        self.toolButton_4.setText(_translate("Form", "delete or edit"))
        self.toolButton_5.setText(_translate("Form", "design pattern of carprt"))
        self.toolButton_6.setText(_translate("Form", "change pattern of carpets"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

