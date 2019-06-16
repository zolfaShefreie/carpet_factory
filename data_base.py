import factory_info_action
import sale_service
import os
import ast
from PIL import Image
import numpy as np
from resizeimage import resizeimage

class dataBase:
    # paini ham zakhire  kon img_path
    img_path=[]
    # {name:[price,address_file]}
    img_and_price={}
    factory_func=factory_info_action.info_func()
    sale_func=sale_service.sale_service()
    def __init__(self):
        self.load()
    
    def is_it_image(self,file):
        try:
            img=Image.open(file)
        except Exception:
            return False
        return True
    
    def most_similar(self,matrix_base):
        returns=[]
        return_list=[]
        for each in self.img_and_price.values():
            self.resize_image(each[1], save_file="./sec_img_compare.jpg", w=40, h=30)
            matrix_sec=self.image_to_matrix("./sec_img_compare.jpg")
            returns.append(self.sale_func.min_penalty(matrix_base, matrix_sec))
            
        for i in range(0,3):
            return_list.append(returns.index(sorted(returns)[i]))
            
        return return_list
    
    def image_to_matrix(self,file):
        try:
            img=Image.open(file)
        except Exception:
            pass
        matrix=np.asanyarray(img, dtype=int)
        matrix=matrix.tolist()
        if len(matrix[0][0])==3:
            for i in range(0,len(matrix)):
                for j in range(0,len(matrix[0])):
                    hex_color='{:02x}{:02x}{:02x}'.format( matrix[i][j][0], matrix[i][j][1] , matrix[i][j][2])
                    matrix[i][j]=hex_color
        elif  len(matrix[0][0])==4:
            for i in range(0,len(matrix)):
                for j in range(0,len(matrix[0])):
                    hex_color='{:02x}{:02x}{:02x}{:02x}'.format( matrix[i][j][0], matrix[i][j][1] , matrix[i][j][2], matrix[i][j][3] )
                    matrix[i][j]=hex_color
        
        return matrix
    
    def resize_image(self,file,save_file="",w=400,h=300):
        if save_file=="":
            save_file=file
        file=str(file)
        with open(file, 'r+b') as ff:
            with Image.open(ff) as image:
                cover = resizeimage.resize_cover(image, [w, h],validate=False)
                cover.save(save_file, image.format)
        
    
    def fill_with_black_cut(self,matrix=[[0]]):
        #300 * 400
        if len(matrix)==0:
            raise Exception("the input isn't matrix")
        elif len(matrix[0])==0:
            raise Exception("it isn't 2d matrix")
        if len(matrix)>300:
            matrix=matrix[0:301]
        if len(matrix[0])>400:
            for i in range(0,len(matrix)):
                matrix[i]=matrix[i][0:401]
        black_list=[]
        for i in range (0,len(matrix)):
            for j in range(len(matrix[0]),400):
                matrix[i].append("000000")
        
        for  i in range(0,400):
            black_list.append("000000")
        
        for i in range(len(matrix),300):
            matrix.append(black_list)
        
        return matrix
            
    def matrix_to_image(self,matrix):
        #deraieha bayad be sorate hex o string bashan
        if len(matrix)==0:
            raise Exception("the input isn't matrix")
        elif len(matrix[0])==0:
            raise Exception("it isn't 2d matrix")
        
        if len(matrix[0][0])==6:
        
            for each in range(0,len(matrix)):
                for each1 in range(0,len(matrix[0])):
                    hex_color=matrix[each][each1]
                    rgb_color=list(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                    matrix[each][each1]=rgb_color

            
        elif len(matrix[0][0])==8:
            for each in range(0,len(matrix)):
                for each1 in range(0,len(matrix[0])):
                    hex_color=matrix[each][each1]
                    rgb_color=list(int(hex_color[i:i+2], 16) for i in (0, 2, 4, 6))
                    matrix[each][each1]=rgb_color
                    
        matrix=np.array(matrix,dtype=np.uint8)
        img = Image.fromarray(matrix, 'RGB')
        img.save('strassen_result.jpg')
        
        
        
    
    def load(self):
#         path = os.getcwd()
#         img_dir=os.path.join(path,"img")
#         if img_dir in os.listdir(path):
#             for each in os.listdir(img_dir):
#                 new_path=path+"/"+str(each)
#                 self.img_path.append(new_path)
#         else:
#             try:
#                 os.mkdir(img_dir)
#             except OSError:
#                 pass
#         self.factory_func.address.load()
        try:
            info=open("./info.txt", 'r')
            txt=info.read()
            self.img_and_price = ast.literal_eval(txt)
            info.close()
            self.factory_func.address.load()
                
        except OSError and FileNotFoundError:
            pass

            
    
    def exit_save(self):
        self.save()
        self.factory_func.address.save()
    
    def save(self):
        info=open("./info.txt", 'w')
        info.write(str(self.img_and_price))
        info.close()
    
    def __del__(self):
        self.exit_save()