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
from matplotlib import colors as mcolors
from PyQt5.Qt import QMessageBox
import shutil
import os
from PIL import Image

class Ui_Form(object):
    aliki_list=[]
    
    data=data_base.dataBase()
    fac_list=[]
    ins_list=[]
    edges=[]
    part_carpet=[]
    carpet_edge=[]
    standard_carpet_edge=[]
    color_list= dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    color_list=list(color_list.keys())
    color_list=color_list[8:]
    count=0
    min=0
    
    def change_pattern(self):
        self.stackedWidget.setCurrentIndex(9)
        
    
    def strasseen_gui(self):
        address1=self.lineEdit_5.text()
        address2=self.lineEdit_8.text()
        
        try:
            image1=Image.open(address1)
            image2=Image.open(address2)
        except Exception as e:
            print(e)
        
            
        self.data.resize_image(address1)
        self.data.resize_image(address2)
          
            
        image_matrix1=self.data.image_to_matrix(address1)
        image_matrix2=self.data.image_to_matrix(address2)
        
                    
        for i in range(300):
            for j in range(400):
                image_matrix1[i][j]=int(image_matrix2[i][j],16)
                    
        for i in range(300):
            for j in range(400):
                image_matrix2[i][j]=int(image_matrix2[i][j],16)
                    
        for i in range(300,512):
            image_matrix1.append([0 for k in range(512)])
    
        for i in range(300):
            for j in range(400,512):
                image_matrix1[i].append(0)
                    
        for i in range(300,512):
            image_matrix2.append([0 for k in range(512)])
    
        for i in range(300):
            for j in range(400,512):
                image_matrix2[i].append(0)
        try:        
            result_strassen=self.data.factory_func.strassen(image_matrix1,image_matrix2)
        
            result_strassen=result_strassen[0:300]
            for i in range(300):
                result_strassen[i]=result_strassen[i][0:400]
        
            hex_result=[['']*400 for i in range(300)]
   
            for i in range(300):
                for j in range(400):
                    h=hex((result_strassen[i][j]))
                    h=h[2:]
                    if len(h)<=6:
                        h=h.zfill(6)
                    else:
                        h=h[len(h)-6:]
                    hex_result[i][j]=h
            print('finish')
            
            self.data.matrix_to_image(hex_result)
            self.img=QtGui.QImage("./strassen_result.jpg")
            self.pic=QtGui.QPixmap.fromImage(self.img)
            self.pixmap5 = self.pic.scaled(self.label_21.width(), self.label_21.height())
            self.label_21.setPixmap(self.pixmap5)
            self.stackedWidget.setCurrentIndex(10)
            
        except Exception  as e:
            print(e)
        
#         f=open("./h.txt",'w')
#         f.write(str(int_result))
    def yse_save(self):
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.stackedWidget.setCurrentIndex(11)
    
    def no_save(self):
        self.lineEdit_5.clear()
        self.lineEdit_8.clear()
        self.stackedWidget.setCurrentIndex(2)
        
    def ok_enter_price_name(self):
        name=self.lineEdit_6.text()
        price=self.lineEdit_7.text()
        
        try:
            price=int(price)
            img=Image.open('./strassen_result.jpg')
            img.close()
            if name not in self.data.img_and_price :
                os.rename('strassen_result.jpg',str(name)+'.jpg')
                new=shutil.copy('./'+str(name)+'.jpg', './img')
                self.data.resize_image(new)
                self.data.img_and_price[name]=[0,'']
                self.data.img_and_price[name][0]=price
                self.data.img_and_price[name][1]=str(new)
                self.data.exit_save()
                self.stackedWidget.setCurrentIndex(2)
            else:
                self.message.setText("there is another carpet with this name please enter new name")
                self.message.setStandardButtons(QMessageBox.Ok)
                self.message.show()
                self.message.buttonClicked.connect(self.message.close)
        except Exception as e:
            print(e)
            self.message.setText('price must be int')
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
            

    #koole poshti
    def get_budget(self):
        
        budget_string=self.lineEdit_4.text()
        budget_int=int(budget_string)
#         if len(self.data.img_and_price)==0:
#             self.message.setText("NO CARPETS YET")
#             self.message.setStandardButtons(QMessageBox.Ok)
#             self.message.show()
#             self.message.buttonClicked.connect(self.message.close)
#             self.stackedWidget.setCurrentIndex(7)
        
        a,b=self.data.sale_func.maximum_carpets(budget_int,self.data.img_and_price)
        self.stackedWidget.setCurrentIndex(8)
        txt=self.label_18.text()+" "+str(a)
        self.label_18.setText(txt)
        self.listWidget_7.addItems(b)
#             self.label_18.setText("maximum carpets you can buy: "+str(a)+2*"\n"+"carpets: "+str(b))

    def ok_button_9(self):
        self.listWidget_7.clear()
        self.stackedWidget.setCurrentIndex(1)

    def money_button(self):
        if len(self.data.img_and_price)==0:
            self.message.setText("NO CARPETS YET")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
        else:    
            self.stackedWidget.setCurrentIndex(7)

    def ok_budget(self):
        self.stackedWidget.setCurrentIndex(8)

# main pages
    
    def search_by_pattern(self):
        if len(self.data.img_and_price)>=3:
            self.stackedWidget.setCurrentIndex(21)
        else:
            self.message.setText("there isn't enough carpet to do this")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
        
    def anwer_sale_button(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def anwer_fact_button(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def back_click(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def change_make_address(self):
        self.stackedWidget.setCurrentIndex(3)
        
    def find_nearest_path(self):
        if self.data.factory_func.address.is_empty():
            self.message.setText("the address doesn't exist")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
        else:
            self.stackedWidget.setCurrentIndex(12)
            for each in self.data.factory_func.address.inst_nodes:
                self.list_inst_sale.addItem(str(each))
            
            self.img=QtGui.QImage("./Graph.png")
            self.pic=QtGui.QPixmap.fromImage(self.img)
            self.pixmap5 = self.pic.scaled(self.show_graph.width(), self.show_graph.height())
            self.show_graph.setPixmap(self.pixmap5)
    
    def answer_delete(self):
        self.stackedWidget.setCurrentIndex(18)
        
    def create_pattern(self):
        self.stackedWidget.setCurrentIndex(14)
        
# add address
        
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
            self.edges=[[0]*(len(self.fac_list)+len(self.ins_list)) for i in range((len(self.fac_list)+len(self.ins_list)))]
#             list_alaki=[0 for i in range(0,(len(self.fac_list)+len(self.ins_list)))]
#                 
#             self.edges=[list_alaki for i in range(0,(len(self.fac_list)+len(self.ins_list)))]
                
                
            for each in self.ins_list:
                self.listWidget_4.addItem(str(each))
                self.listWidget_5.addItem(str(each))
            for each in self.fac_list:
                self.listWidget_4.addItem(str(each))
                self.listWidget_5.addItem(str(each))
                
    def answer_add_edges(self):
        row=self.listWidget_4.currentRow()
        column=self.listWidget_5.currentRow()
        if self.listWidget_4.currentRow()!= -1 and self.listWidget_5.currentRow() != -1 and self.lineEdit_3.text().split() != ''  and row!=column:
            txt=self.lineEdit_3.text()

            try:
                txt=int(txt)
                if txt != 0:
                    self.edges[row][column]=txt
                    self.edges[column][row]=txt
                else:
                    self.message.setText("distance cant be 0")
                    self.message.setStandardButtons(QMessageBox.Ok)
                    self.message.show()
                    self.message.buttonClicked.connect(self.message.close)
                    self.lineEdit_3.clear()
            except Exception as error:
                self.message.setText(str(txt))
                self.message.setStandardButtons(QMessageBox.Ok)
                self.message.show()
                self.message.buttonClicked.connect(self.message.close)
                self.lineEdit_3.clear()
        else:
            self.message.setText("you should select two different nodes and write the distance of between them")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
        self.lineEdit_3.clear()
            
    def answer_next_click3(self):
        
        self.message.setText("the data is saved")
        self.message.setStandardButtons(QMessageBox.Ok)
        self.message.show()
        self.message.buttonClicked.connect(self.message.close)
        self.data.exit_save()
        self.stackedWidget.setCurrentIndex(6)
        self.listWidget_4.clear()
        self.listWidget_5.clear()
 

        self.data.factory_func.address.fac_nodes=self.fac_list
        self.data.factory_func.address.inst_nodes=self.ins_list
        self.data.factory_func.address.edges=self.edges
        edges_list=self.data.factory_func.address.edges_list()
        nodes=self.data.factory_func.address.inst_nodes+self.data.factory_func.address.fac_nodes

        
        G=nx.Graph()

        G.add_nodes_from(nodes)
        try:
            G.add_weighted_edges_from(edges_list)
        except  Exception as e:
            print(e)
            print("33333333")
         
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
        self.stackedWidget.setCurrentIndex(2)
        
    # sale: find nearest path
    def select_a_node(self):
        row = self.list_inst_sale.currentRow()
        if row!=-1:
            try:
                node=self.data.factory_func.address.inst_nodes[row]
                path_dict=self.data.factory_func.address.shortest_path(node)
                list_alaki=path_dict[next(iter(path_dict))]
                self.address_1.setText(str(list_alaki))
                self.nearest_factory.setText(list_alaki[-1])
                self.stackedWidget.setCurrentIndex(13)
                color_edget=[]
                edges_list=self.data.factory_func.address.edges_list()
                nodes=self.data.factory_func.address.inst_nodes+self.data.factory_func.address.fac_nodes
            except Exception as e:
                print(e)    
            G=nx.Graph()
            G.add_nodes_from(nodes)
            G.add_weighted_edges_from(edges_list)
         
            color=[]
            for i in range(0,len(self.data.factory_func.address.fac_nodes)):
                color.append('red')
            for i in range(0,len(self.data.factory_func.address.inst_nodes)):
                color.append('blue')
                
            list_convert=self.data.factory_func.address.convert(path_dict)
            for each in edges_list:
                if each in list_convert:
                    color_edget.append('red')
                else:
                    color_edget.append('black')
         
            nx.draw_circular(G,edge_color=color_edget,node_color = color,with_labels=True,node_size=1000,alpha=1)
            plt.savefig("./Graph_find.png", format="PNG")
            self.img=QtGui.QImage("./Graph_find.png")
            self.pic=QtGui.QPixmap.fromImage(self.img)
            self.pixmap5 = self.pic.scaled(self.grath_to_factor.width(), self.grath_to_factor.height())
            self.grath_to_factor.setPixmap(self.pixmap5)
            
        else:
            self.message.setText("you didn't select one")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
 
    def answer_got_it(self):
        self.stackedWidget.setCurrentIndex(1)
        
    # add delete edit
    def add_new_ca(self):
        self.stackedWidget.setCurrentIndex(20)
        
    def add_carpet_click(self):
        file=self.lineEdit_11.text()
        name=self.lineEdit_12.text()
        price=self.lineEdit_13.text()
        if len(name.split())==0:
            self.message.setText("the name is empty")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
        else:
            try:
                price=int(price)
                if name not in self.data.img_and_price:
                    img=Image.open(file)
                    new=shutil.copy(file, './img')
                    self.data.resize_image(new)
                    self.data.img_and_price[name]=[0,'']
                    self.data.img_and_price[name][0]=price
                    self.data.img_and_price[name][1]=str(new)
                else:
                    self.message.setText("there is another carpet with this name please enter new name")
                    self.message.setStandardButtons(QMessageBox.Ok)
                    self.message.show()
                    self.message.buttonClicked.connect(self.message.close)
                
            except Exception as error:
                self.message.setText(str(error))
                self.message.setStandardButtons(QMessageBox.Ok)
                self.message.show()
                self.message.buttonClicked.connect(self.message.close)
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()
    
    def finish_adding(self):
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()
        self.data.exit_save()
        self.stackedWidget.setCurrentIndex(2)
      
    def delete_edit(self):
        self.listWidget_6.clear()
        self.stackedWidget.setCurrentIndex(19)
        for each in self.data.img_and_price.keys():
            self.listWidget_6.addItem(str(each))
        
    def delete_button_click(self):
        row=self.listWidget_6.currentRow()
        if row!=-1:
            key=self.listWidget_6.item(row)
            try:
                os.remove(self.data.img_and_price[key.text()][1])
            except Exception :
                pass
            del self.data.img_and_price[key.text()]
            self.listWidget_6.takeItem(row)

        else:
            self.message.setText("select the carpet")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
            
    def finish_deleting(self):
        self.data.exit_save()
        self.stackedWidget.setCurrentIndex(2)
        
    def edit(self):
        row=self.listWidget_6.currentRow()
        txt=self.lineEdit_10.text()
        if row!=-1:
            try:
                txt=int(txt)
                key=self.listWidget_6.item(row)
                self.data.img_and_price[key.text()][0]=txt
            except Exception as error:
                self.message.setText("the price is invalid")
                self.message.setStandardButtons(QMessageBox.Ok)
                self.message.show()
                self.message.buttonClicked.connect(self.message.close)
        else:
            self.message.setText("select the carpet")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
                
    # graph coloring
    def add_node_part(self):
        text=self.lineEdit_9.text()
        text1=text.split()
        text=text.lower()
        if text not in self.part_carpet and len(text1)!=0:
            self.part_carpet.append(text)
            self.listWidget_2.addItem(text)
         
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
            
        self.lineEdit_9.clear()
    def next_part(self):
        if self.listWidget_2.count() == 0:
            self.message.setText("the list of nodes is empty")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
        else:
            self.stackedWidget.setCurrentIndex(15)
            self.listWidget_2.clear()
            self.standard_carpet_edge=[[0]*(len(self.part_carpet)) for i in range(len(self.part_carpet))]
                
            for each in self.part_carpet:
                self.part1.addItem(str(each))
                self.part2.addItem(str(each))
    def add_edge_part(self):
        row=self.part1.currentRow()
        column=self.part2.currentRow()
        if row!=-1 and column!=-1 and row!=column:
            if (self.part_carpet[row],self.part_carpet[column]) not in self.carpet_edge and (self.part_carpet[column],self.part_carpet[row])not in self.carpet_edge:
                self.carpet_edge.append((self.part_carpet[row],self.part_carpet[column]))
                self.standard_carpet_edge[row][column]=1
                self.standard_carpet_edge[column][row]=1
            else:
                self.message.setText("it added before")
                self.message.setStandardButtons(QMessageBox.Ok)
                self.message.show()
                self.message.buttonClicked.connect(self.message.close)
        else :
            self.message.setText("you should select two different nodes")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)

    def next_of_adding_edge_part(self):
        self.part1.clear()
        self.part2.clear()
        self.stackedWidget.setCurrentIndex(16)
        try:
            colors=self.data.factory_func.first_input(len(self.part_carpet))
            self.data.factory_func.grath_coloring(-1,colors,self.standard_carpet_edge,len(self.part_carpet))
            result=self.data.factory_func.result_grath_coloring
            self.min=self.data.factory_func.min_color(len(self.part_carpet))
            self.label_32.setText(str(self.min))
            
#         color_list= dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
#         color_list=list(color_list.keys())
#         color_list=color_list[8:]
#             for each in self.color_list:
#                 self.list_color.addItems(str(each))
            self.list_color.addItems(self.color_list)
        except Exception as e:
            print(e)
     
    def got_back(self):
        self.stackedWidget.setCurrentIndex(2)
        self.data.factory_func.result_grath_coloring.clear()
            
    def add_color(self):
        if self.count<self.min:
            row=self.list_color.currentRow()
            if self.color_list[row] in self.aliki_list:
                self.message.setText("it is chosen before")
                self.message.setStandardButtons(QMessageBox.Ok)
                self.message.show()
                self.message.buttonClicked.connect(self.message.close)
            else:
                self.aliki_list.append(self.color_list[row])
                self.count+=1
        
        else:
            self.pushButton_21.setText("finish")
            self.stackedWidget.setCurrentIndex(17)
            G=nx.Graph()
            G.add_nodes_from(self.part_carpet)
        #G.add_node("hi")
            G.add_edges_from(self.carpet_edge)
        #G.combinatorial_embedding_to_pos()
    
        
            color=self.aliki_list

        #G.combinatorial_embedding_to_pos()
            nx.draw(G,node_color = color,with_labels=True,node_size=6000,alpha=1)
            plt.savefig("Graph_coloring.png", format="PNG")
            img=QtGui.QImage("./Graph_coloring.png")
            pic=QtGui.QPixmap.fromImage(img)
            pixmap5 = pic.scaled(self.graph_coloring.width(), self.graph_coloring.height())
            self.graph_coloring.setPixmap(pixmap5)
            self.data.factory_func.result_grath_coloring.clear()
    def ok_end(self):
        self.count=0
        self.list_color.clear()
        self.min=0
        self.standard_carpet_edge.clear()
        self.part_carpet.clear()
        self.carpet_edge.clear()
        self.aliki_list.clear()
        self.stackedWidget.setCurrentIndex(2)
        
    # sequence alignment
    def get_the_path(self):
        text=self.lineEdit_14.text()
         
        if text=="":
            self.message.setText("line edit is empty")
            self.message.setStandardButtons(QMessageBox.Ok)
            self.message.show()
            self.message.buttonClicked.connect(self.message.close)
        
        else:
            try:
                img_check=Image.open(text)
                self.data.resize_image(text,save_file="./base_img_compare.jpg",w=40,h=30)
                matrix=self.data.image_to_matrix("./base_img_compare.jpg")
                return_list=self.data.most_similar(matrix)
                
                name=list(self.data.img_and_price)[return_list[0]]
                price_file=list(self.data.img_and_price.values())[return_list[0]]
                self.label_51.setText(str(name))
                self.label_52.setText(str(price_file[0]))
                img=QtGui.QImage(str(price_file[1]))
                pic=QtGui.QPixmap.fromImage(img)
                pixmap5 = pic.scaled(self.label_42.width(), self.label_42.height())
                self.label_42.setPixmap(pixmap5)
                
                name=list(self.data.img_and_price)[return_list[1]]
                price_file=list(self.data.img_and_price.values())[return_list[1]]
                self.label_56.setText(str(name))
                self.label_55.setText(str(price_file[0]))
                img=QtGui.QImage(str(price_file[1]))
                pic=QtGui.QPixmap.fromImage(img)
                pixmap5 = pic.scaled(self.label_43.width(), self.label_43.height())
                self.label_43.setPixmap(pixmap5)
                
                name=list(self.data.img_and_price)[return_list[2]]
                price_file=list(self.data.img_and_price.values())[return_list[2]]
                self.label_54.setText(str(name))
                self.label_53.setText(str(price_file[0]))
                img=QtGui.QImage(str(price_file[1]))
                pic=QtGui.QPixmap.fromImage(img)
                pixmap5 = pic.scaled(self.label_44.width(), self.label_44.height())
                self.label_44.setPixmap(pixmap5)
                
                
            except Exception as error:
                self.lineEdit_14.clear()
                self.message.setText(error)
                self.message.setStandardButtons(QMessageBox.Ok)
                self.message.show()
                self.message.buttonClicked.connect(self.message.close)  
                
    def ok_to_finish(self):
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
        self.label_17.setGeometry(QtCore.QRect(130, 170, 171, 21))
        self.label_17.setObjectName("label_17")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_8)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 170, 251, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 300, 221, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.background_nearest_8 = QtWidgets.QLabel(self.page_8)
        self.background_nearest_8.setGeometry(QtCore.QRect(170, 0, 491, 451))
        self.background_nearest_8.setStyleSheet("background-image: url(./background/background3.jpg);")
        self.background_nearest_8.setText("")
        self.background_nearest_8.setObjectName("background_nearest_8")
        self.background_nearest_8.raise_()
        self.label_17.raise_()
        self.lineEdit_4.raise_()
        self.pushButton_8.raise_()
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_9.setGeometry(QtCore.QRect(450, 190, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.listWidget_7 = QtWidgets.QListWidget(self.page_9)
        self.listWidget_7.setGeometry(QtCore.QRect(60, 80, 256, 341))
        self.listWidget_7.setObjectName("listWidget_7")
        self.label_18 = QtWidgets.QLabel(self.page_9)
        self.label_18.setGeometry(QtCore.QRect(60, 50, 281, 16))
        self.label_18.setObjectName("label_18")
        self.label_57 = QtWidgets.QLabel(self.page_9)
        self.label_57.setGeometry(QtCore.QRect(270, 0, 511, 451))
        self.label_57.setStyleSheet("background-image: url(./background/background1.jpg);")
        self.label_57.setText("")
        self.label_57.setObjectName("label_57")
        self.label_57.raise_()
        self.pushButton_9.raise_()
        self.listWidget_7.raise_()
        self.label_18.raise_()
        self.stackedWidget.addWidget(self.page_9)

        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_19 = QtWidgets.QLabel(self.page_10)
        self.label_19.setGeometry(QtCore.QRect(70, 150, 131, 16))
        self.label_19.setObjectName("label_19")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_10)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 150, 431, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_25 = QtWidgets.QLabel(self.page_10)
        self.label_25.setGeometry(QtCore.QRect(70, 230, 141, 21))
        self.label_25.setObjectName("label_25")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_10)
        self.lineEdit_8.setGeometry(QtCore.QRect(270, 230, 431, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_14.setGeometry(QtCore.QRect(300, 300, 111, 28))
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_20 = QtWidgets.QLabel(self.page_10)
        self.label_20.setGeometry(QtCore.QRect(240, 70, 251, 20))
        self.label_20.setObjectName("label_20")
        self.label_58 = QtWidgets.QLabel(self.page_10)
        self.label_58.setGeometry(QtCore.QRect(270, 0, 511, 451))
        self.label_58.setStyleSheet("background-image: url(./background/background1.jpg);")
        self.label_58.setText("")
        self.label_58.setObjectName("label_58")
        self.label_58.raise_()
        self.label_19.raise_()
        self.lineEdit_5.raise_()
        self.label_25.raise_()
        self.lineEdit_8.raise_()
        self.pushButton_14.raise_()
        self.label_20.raise_()
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.label_21 = QtWidgets.QLabel(self.page_11)
        self.label_21.setGeometry(QtCore.QRect(40, 20, 691, 271))
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page_11)
        self.label_22.setGeometry(QtCore.QRect(140, 370, 221, 21))
        self.label_22.setObjectName("label_22")
        self.pushButton_11 = QtWidgets.QPushButton(self.page_11)
        self.pushButton_11.setGeometry(QtCore.QRect(400, 370, 93, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.page_11)
        self.pushButton_12.setGeometry(QtCore.QRect(500, 370, 93, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.label_23 = QtWidgets.QLabel(self.page_12)
        self.label_23.setGeometry(QtCore.QRect(140, 100, 101, 21))
        self.label_23.setObjectName("label_23")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_12)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 100, 391, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_24 = QtWidgets.QLabel(self.page_12)
        self.label_24.setGeometry(QtCore.QRect(140, 240, 111, 21))
        self.label_24.setObjectName("label_24")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_12)
        self.lineEdit_7.setGeometry(QtCore.QRect(300, 240, 381, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_12)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 340, 111, 28))
        self.pushButton_13.setObjectName("pushButton_13")
        self.background_nearest_9 = QtWidgets.QLabel(self.page_12)
        self.background_nearest_9.setGeometry(QtCore.QRect(0, 0, 491, 451))
        self.background_nearest_9.setStyleSheet("background-image: url(./background/background3.jpg);")
        self.background_nearest_9.setText("")
        self.background_nearest_9.setObjectName("background_nearest_9")
        self.background_nearest_9.raise_()
        self.label_23.raise_()
        self.lineEdit_6.raise_()
        self.label_24.raise_()
        self.lineEdit_7.raise_()
        self.pushButton_13.raise_()
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.background_nearest_1 = QtWidgets.QLabel(self.page_13)
        self.background_nearest_1.setGeometry(QtCore.QRect(0, 0, 491, 451))
        self.background_nearest_1.setStyleSheet("background-image: url(./background/background2.jpg);")
        self.background_nearest_1.setText("")
        self.background_nearest_1.setObjectName("background_nearest_1")
        self.show_graph = QtWidgets.QLabel(self.page_13)
        self.show_graph.setGeometry(QtCore.QRect(440, 0, 341, 441))
        self.show_graph.setText("")
        self.show_graph.setObjectName("show_graph")
        self.label_27 = QtWidgets.QLabel(self.page_13)
        self.label_27.setGeometry(QtCore.QRect(80, 50, 281, 16))
        self.label_27.setObjectName("label_27")
        self.list_inst_sale = QtWidgets.QListWidget(self.page_13)
        self.list_inst_sale.setGeometry(QtCore.QRect(100, 80, 256, 321))
        self.list_inst_sale.setObjectName("list_inst_sale")
        self.pushButton_15 = QtWidgets.QPushButton(self.page_13)
        self.pushButton_15.setGeometry(QtCore.QRect(104, 410, 251, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.background_nearest_2 = QtWidgets.QLabel(self.page_14)
        self.background_nearest_2.setGeometry(QtCore.QRect(0, 0, 491, 451))
        self.background_nearest_2.setStyleSheet("background-image: url(./background/background2.jpg);")
        self.background_nearest_2.setText("")
        self.background_nearest_2.setObjectName("background_nearest_2")
        self.grath_to_factor = QtWidgets.QLabel(self.page_14)
        self.grath_to_factor.setGeometry(QtCore.QRect(440, 2, 341, 451))
        self.grath_to_factor.setText("")
        self.grath_to_factor.setObjectName("grath_to_factor")
        self.label_28 = QtWidgets.QLabel(self.page_14)
        self.label_28.setGeometry(QtCore.QRect(80, 80, 101, 21))
        self.label_28.setObjectName("label_28")
        self.nearest_factory = QtWidgets.QLabel(self.page_14)
        self.nearest_factory.setGeometry(QtCore.QRect(240, 80, 181, 16))
        self.nearest_factory.setText("")
        self.nearest_factory.setObjectName("nearest_factory")
        self.label_30 = QtWidgets.QLabel(self.page_14)
        self.label_30.setGeometry(QtCore.QRect(90, 160, 47, 13))
        self.label_30.setObjectName("label_30")
        self.address_1 = QtWidgets.QLabel(self.page_14)
        self.address_1.setGeometry(QtCore.QRect(180, 160, 231, 221))
        self.address_1.setText("")
        self.address_1.setObjectName("address_1")
        self.got = QtWidgets.QPushButton(self.page_14)
        self.got.setGeometry(QtCore.QRect(234, 400, 111, 23))
        self.got.setObjectName("got")
        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.background_nearest_3 = QtWidgets.QLabel(self.page_15)
        self.background_nearest_3.setGeometry(QtCore.QRect(0, 0, 491, 451))
        self.background_nearest_3.setStyleSheet("background-image: url(./background/background3.jpg);")
        self.background_nearest_3.setText("")
        self.background_nearest_3.setObjectName("background_nearest_3")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_15)
        self.lineEdit_9.setGeometry(QtCore.QRect(250, 30, 321, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_26 = QtWidgets.QLabel(self.page_15)
        self.label_26.setGeometry(QtCore.QRect(50, 30, 181, 20))
        self.label_26.setObjectName("label_26")
        self.pushButton_16 = QtWidgets.QPushButton(self.page_15)
        self.pushButton_16.setGeometry(QtCore.QRect(610, 30, 75, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.listWidget_2 = QtWidgets.QListWidget(self.page_15)
        self.listWidget_2.setGeometry(QtCore.QRect(290, 90, 256, 281))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_17 = QtWidgets.QPushButton(self.page_15)
        self.pushButton_17.setGeometry(QtCore.QRect(294, 400, 251, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.stackedWidget.addWidget(self.page_15)
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setObjectName("page_16")
        self.background_nearest_4 = QtWidgets.QLabel(self.page_16)
        self.background_nearest_4.setGeometry(QtCore.QRect(0, 0, 491, 451))
        self.background_nearest_4.setStyleSheet("background-image: url(./background/background3.jpg);")
        self.background_nearest_4.setText("")
        self.background_nearest_4.setObjectName("background_nearest_4")
        self.part1 = QtWidgets.QListWidget(self.page_16)
        self.part1.setGeometry(QtCore.QRect(90, 60, 231, 291))
        self.part1.setObjectName("part1")
        self.part2 = QtWidgets.QListWidget(self.page_16)
        self.part2.setGeometry(QtCore.QRect(460, 60, 241, 291))
        self.part2.setObjectName("part2")
        self.pushButton_18 = QtWidgets.QPushButton(self.page_16)
        self.pushButton_18.setGeometry(QtCore.QRect(264, 370, 241, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.page_16)
        self.pushButton_19.setGeometry(QtCore.QRect(264, 400, 241, 23))
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_29 = QtWidgets.QLabel(self.page_16)
        self.label_29.setGeometry(QtCore.QRect(200, 30, 361, 20))
        self.label_29.setObjectName("label_29")
        self.stackedWidget.addWidget(self.page_16)
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setObjectName("page_17")
        self.background_nearest_5 = QtWidgets.QLabel(self.page_17)
        self.background_nearest_5.setGeometry(QtCore.QRect(0, 0, 491, 451))
        self.background_nearest_5.setStyleSheet("background-image: url(./background/background3.jpg);")
        self.background_nearest_5.setText("")
        self.background_nearest_5.setObjectName("background_nearest_5")
        self.list_color = QtWidgets.QListWidget(self.page_17)
        self.list_color.setGeometry(QtCore.QRect(490, 80, 256, 301))
        self.list_color.setObjectName("list_color")
        self.label_31 = QtWidgets.QLabel(self.page_17)
        self.label_31.setGeometry(QtCore.QRect(60, 200, 141, 20))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.page_17)
        self.label_32.setGeometry(QtCore.QRect(250, 200, 31, 31))
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.pushButton_20 = QtWidgets.QPushButton(self.page_17)
        self.pushButton_20.setGeometry(QtCore.QRect(90, 360, 161, 23))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_17)
        self.pushButton_21.setGeometry(QtCore.QRect(494, 390, 251, 23))
        self.pushButton_21.setObjectName("pushButton_21")
        self.stackedWidget.addWidget(self.page_17)
        self.page_18 = QtWidgets.QWidget()
        self.page_18.setObjectName("page_18")
        self.label_33 = QtWidgets.QLabel(self.page_18)
        self.label_33.setGeometry(QtCore.QRect(300, 40, 201, 16))
        self.label_33.setObjectName("label_33")
        self.graph_coloring = QtWidgets.QLabel(self.page_18)
        self.graph_coloring.setGeometry(QtCore.QRect(210, 80, 391, 301))
        self.graph_coloring.setText("")
        self.graph_coloring.setObjectName("graph_coloring")
        self.pushButton_22 = QtWidgets.QPushButton(self.page_18)
        self.pushButton_22.setGeometry(QtCore.QRect(380, 410, 75, 23))
        self.pushButton_22.setObjectName("pushButton_22")
        self.stackedWidget.addWidget(self.page_18)
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setObjectName("page_20")
        self.background_nearest_6 = QtWidgets.QLabel(self.page_20)
        self.background_nearest_6.setGeometry(QtCore.QRect(80, 0, 491, 451))
        self.background_nearest_6.setStyleSheet("background-image: url(./background/background3.jpg);")
        self.background_nearest_6.setText("")
        self.background_nearest_6.setObjectName("background_nearest_6")
        self.pushButton_26 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_26.setGeometry(QtCore.QRect(220, 130, 301, 23))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_27.setGeometry(QtCore.QRect(220, 290, 301, 23))
        self.pushButton_27.setObjectName("pushButton_27")
        self.stackedWidget.addWidget(self.page_20)
        self.page_19 = QtWidgets.QWidget()
        self.page_19.setObjectName("page_19")
        self.label_34 = QtWidgets.QLabel(self.page_19)
        self.label_34.setGeometry(QtCore.QRect(270, 0, 511, 451))
        self.label_34.setStyleSheet("background-image: url(./background/background1.jpg);")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.listWidget_6 = QtWidgets.QListWidget(self.page_19)
        self.listWidget_6.setGeometry(QtCore.QRect(80, 80, 256, 281))
        self.listWidget_6.setObjectName("listWidget_6")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_19)
        self.lineEdit_10.setGeometry(QtCore.QRect(480, 80, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_35 = QtWidgets.QLabel(self.page_19)
        self.label_35.setGeometry(QtCore.QRect(90, 50, 71, 16))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.page_19)
        self.label_36.setGeometry(QtCore.QRect(410, 80, 51, 20))
        self.label_36.setObjectName("label_36")
        self.pushButton_23 = QtWidgets.QPushButton(self.page_19)
        self.pushButton_23.setGeometry(QtCore.QRect(420, 190, 181, 23))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.page_19)
        self.pushButton_24.setGeometry(QtCore.QRect(420, 250, 181, 23))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.page_19)
        self.pushButton_25.setGeometry(QtCore.QRect(420, 310, 181, 23))
        self.pushButton_25.setObjectName("pushButton_25")
        self.stackedWidget.addWidget(self.page_19)
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setObjectName("page_21")
        self.label_37 = QtWidgets.QLabel(self.page_21)
        self.label_37.setGeometry(QtCore.QRect(160, 90, 71, 16))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.page_21)
        self.label_38.setGeometry(QtCore.QRect(270, 0, 511, 451))
        self.label_38.setStyleSheet("background-image: url(./background/background1.jpg);")
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.page_21)
        self.label_39.setGeometry(QtCore.QRect(160, 140, 81, 16))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.page_21)
        self.label_40.setGeometry(QtCore.QRect(160, 200, 71, 16))
        self.label_40.setObjectName("label_40")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_21)
        self.lineEdit_11.setGeometry(QtCore.QRect(260, 90, 381, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_21)
        self.lineEdit_12.setGeometry(QtCore.QRect(260, 140, 381, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_21)
        self.lineEdit_13.setGeometry(QtCore.QRect(262, 200, 381, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton_28 = QtWidgets.QPushButton(self.page_21)
        self.pushButton_28.setGeometry(QtCore.QRect(250, 300, 301, 23))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.page_21)
        self.pushButton_29.setGeometry(QtCore.QRect(250, 360, 301, 23))
        self.pushButton_29.setObjectName("pushButton_29")
        self.stackedWidget.addWidget(self.page_21)
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setObjectName("page_22")
        self.pushButton_30 = QtWidgets.QPushButton(self.page_22)
        self.pushButton_30.setGeometry(QtCore.QRect(350, 340, 75, 23))
        self.pushButton_30.setObjectName("pushButton_30")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_22)
        self.lineEdit_14.setGeometry(QtCore.QRect(340, 190, 321, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_41 = QtWidgets.QLabel(self.page_22)
        self.label_41.setGeometry(QtCore.QRect(210, 190, 101, 16))
        self.label_41.setObjectName("label_41")
        self.background_nearest_7 = QtWidgets.QLabel(self.page_22)
        self.background_nearest_7.setGeometry(QtCore.QRect(0, 0, 491, 451))
        self.background_nearest_7.setStyleSheet("background-image: url(./background/background2.jpg);")
        self.background_nearest_7.setText("")
        self.background_nearest_7.setObjectName("background_nearest_7")
        self.background_nearest_7.raise_()
        self.pushButton_30.raise_()
        self.lineEdit_14.raise_()
        self.label_41.raise_()
        self.stackedWidget.addWidget(self.page_22)
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.label_42 = QtWidgets.QLabel(self.page_23)
        self.label_42.setGeometry(QtCore.QRect(20, 10, 221, 221))
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.page_23)
        self.label_43.setGeometry(QtCore.QRect(280, 10, 221, 221))
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.page_23)
        self.label_44.setGeometry(QtCore.QRect(540, 10, 221, 221))
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.page_23)
        self.label_45.setGeometry(QtCore.QRect(30, 260, 47, 13))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.page_23)
        self.label_46.setGeometry(QtCore.QRect(280, 260, 47, 13))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.page_23)
        self.label_47.setGeometry(QtCore.QRect(540, 260, 47, 13))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.page_23)
        self.label_48.setGeometry(QtCore.QRect(30, 300, 47, 13))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.page_23)
        self.label_49.setGeometry(QtCore.QRect(540, 290, 47, 13))
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.page_23)
        self.label_50.setGeometry(QtCore.QRect(280, 300, 47, 13))
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.page_23)
        self.label_51.setGeometry(QtCore.QRect(110, 260, 111, 16))
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.page_23)
        self.label_52.setGeometry(QtCore.QRect(100, 290, 111, 16))
        self.label_52.setText("")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.page_23)
        self.label_53.setGeometry(QtCore.QRect(620, 300, 111, 16))
        self.label_53.setText("")
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.page_23)
        self.label_54.setGeometry(QtCore.QRect(620, 260, 111, 16))
        self.label_54.setText("")
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.page_23)
        self.label_55.setGeometry(QtCore.QRect(360, 300, 111, 16))
        self.label_55.setText("")
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.page_23)
        self.label_56.setGeometry(QtCore.QRect(360, 260, 111, 16))
        self.label_56.setText("")
        self.label_56.setObjectName("label_56")
        self.pushButton_31 = QtWidgets.QPushButton(self.page_23)
        self.pushButton_31.setGeometry(QtCore.QRect(234, 370, 331, 23))
        self.pushButton_31.setObjectName("pushButton_31")
        self.stackedWidget.addWidget(self.page_23)


        self.message=QtWidgets.QMessageBox()

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.message.setWindowTitle("system message")
        #Form.setWindowTitle("carpet factory")
        
        #main pages
        self.toolButton.clicked.connect(self.anwer_sale_button)
        self.toolButton_2.clicked.connect(self.anwer_fact_button)
        self.back.clicked.connect(self.back_click)
        self.toolButton_7.clicked.connect(self.back_click)
        self.toolButton_3.clicked.connect(self.change_make_address)
        self.toolButton_10.clicked.connect(self.find_nearest_path)
        self.toolButton_4.clicked.connect(self.answer_delete)
        self.toolButton_5.clicked.connect(self.create_pattern)
        self.toolButton_8.clicked.connect(self.search_by_pattern)
        self.toolButton_6.clicked.connect(self.change_pattern)
        
        #add_address
        self.pushButton.clicked.connect(self.answer_add_click1)
        self.pushButton_2.clicked.connect(self.answer_next_click1)
        self.pushButton_3.clicked.connect(self.answer_add_click2)
        self.pushButton_4.clicked.connect(self.answer_next_click2)
        self.pushButton_5.clicked.connect(self.answer_add_edges)
        self.pushButton_6.clicked.connect(self.answer_next_click3)
        self.pushButton_7.clicked.connect(self.answer_ok_click)
        # show the nearest path
        self.pushButton_15.clicked.connect(self.select_a_node)
        self.got.clicked.connect(self.answer_got_it)
        #edit delete add a carpet
        self.pushButton_26.clicked.connect(self.add_new_ca)
        self.pushButton_27.clicked.connect(self.delete_edit)
        self.pushButton_28.clicked.connect(self.add_carpet_click)
        self.pushButton_29.clicked.connect(self.finish_adding)
        self.pushButton_24.clicked.connect(self.delete_button_click)
        self.pushButton_23.clicked.connect(self.edit)
        self.pushButton_25.clicked.connect(self.finish_deleting)
        #graph_coloring
        self.pushButton_16.clicked.connect(self.add_node_part)
        self.pushButton_17.clicked.connect(self.next_part)
        self.pushButton_18.clicked.connect(self.add_edge_part)
        self.pushButton_19.clicked.connect(self.next_of_adding_edge_part)
        self.pushButton_20.clicked.connect(self.got_back)
        self.pushButton_21.clicked.connect(self.add_color)
        self.pushButton_22.clicked.connect(self.ok_end)
        
        # sequence alignment
        self.pushButton_30.clicked.connect(self.get_the_path)
        self.pushButton_31.clicked.connect(self.ok_to_finish)
        
        #ezafe shode
        self.toolButton_9.clicked.connect(self.money_button)
        self.pushButton_8.clicked.connect(self.ok_budget)
        #@@@KOOLEPOSHTI
        self.pushButton_8.clicked.connect(self.get_budget)
        self.pushButton_9.clicked.connect(self.ok_button_9)
        
        #strassen
        self.pushButton_14.clicked.connect(self.strasseen_gui)
        self.pushButton_11.clicked.connect(self.yse_save)
        self.pushButton_12.clicked.connect(self.no_save)
        self.pushButton_13.clicked.connect(self.ok_enter_price_name)
        
#         Form.destroyed.connect(self.closeE)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "sale services"))
        self.toolButton_2.setText(_translate("Form", "save  data"))
        self.toolButton_8.setText(_translate("Form", "search based on pattern"))
        self.toolButton_9.setText(_translate("Form", "search based on moeny"))
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
        self.label_18.setText(_translate("Form", "max of number of carpet that you can buy is:"))
        self.label_19.setText(_translate("Form", "  enter address of image1:"))
        self.label_25.setText(_translate("Form", "  enter address of image 2:"))
        self.pushButton_14.setText(_translate("Form", "ok"))
        self.label_20.setText(_translate("Form", "you can enter the path of current folder \'s  images"))
        self.label_22.setText(_translate("Form", "  Do you want to save this image?"))
        self.pushButton_11.setText(_translate("Form", "YES"))
        self.pushButton_12.setText(_translate("Form", "NO"))
        self.label_23.setText(_translate("Form", "please  enter name:"))
        self.label_24.setText(_translate("Form", " please enter price:"))
        self.pushButton_13.setText(_translate("Form", "ok"))
        self.label_27.setText(_translate("Form", "please choose the nearest interdrction to yoour location"))
        self.pushButton_15.setText(_translate("Form", "select"))
        self.label_28.setText(_translate("Form", "the nearest factory:"))
        self.label_30.setText(_translate("Form", "address:"))
        self.got.setText(_translate("Form", "i go it"))
        self.label_26.setText(_translate("Form", "please enter the each part Of carpet"))
        self.pushButton_16.setText(_translate("Form", "add"))
        self.pushButton_17.setText(_translate("Form", "next"))
        self.pushButton_18.setText(_translate("Form", "add"))
        self.pushButton_19.setText(_translate("Form", "next"))
        self.label_29.setText(_translate("Form", "please select from two list two part ofcarpet that are beside of eachother"))
        self.label_31.setText(_translate("Form", "the min number of colors is:"))
        self.pushButton_20.setText(_translate("Form", "I got it back to main pages "))
        self.pushButton_21.setText(_translate("Form", "select color"))
        self.label_33.setText(_translate("Form", "a suggestion for coloring the carpet "))
        self.pushButton_22.setText(_translate("Form", "ok"))
        self.pushButton_26.setText(_translate("Form", "add new carpet"))
        self.pushButton_27.setText(_translate("Form", "edit and delete carpet"))
        self.label_35.setText(_translate("Form", "list of carpet"))
        self.label_36.setText(_translate("Form", "new price"))
        self.pushButton_23.setText(_translate("Form", "edit price"))
        self.pushButton_24.setText(_translate("Form", "delete"))
        self.pushButton_25.setText(_translate("Form", "finish"))
        self.label_37.setText(_translate("Form", "address of file"))
        self.label_39.setText(_translate("Form", "name of carpet"))
        self.label_40.setText(_translate("Form", "price"))
        self.pushButton_28.setText(_translate("Form", "add"))
        self.pushButton_29.setText(_translate("Form", "finish"))
        self.pushButton_30.setText(_translate("Form", "next"))
        self.label_41.setText(_translate("Form", "the address  of file"))
        self.label_45.setText(_translate("Form", "name"))
        self.label_46.setText(_translate("Form", "name"))
        self.label_47.setText(_translate("Form", "name"))
        self.label_48.setText(_translate("Form", "price"))
        self.label_49.setText(_translate("Form", "price"))
        self.label_50.setText(_translate("Form", "price"))
        self.pushButton_31.setText(_translate("Form", "ok"))
        
    def closeE(self):
        del self.data
        Form.close()




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

