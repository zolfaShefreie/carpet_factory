import factory_info_action
import sale_service
import os
import ast

class dataBase:
    img_path=[]
    img_and_price={}
    factory_func=factory_info_action.info_func()
    sale_func=sale_service.sale_service()
    def __init__(self):
        path = os.getcwd()
        img_dir=os.path.join(path,"img")
        if img_dir in os.listdir(path):
            for each in os.listdir(img_dir):
                new_path=path+"/"+str(each)
                self.img_path.append(new_path)
        else:
            try:
                os.mkdir(img_dir)
            except OSError:
                pass
        self.factory_func.address.load()
        try:
            info=open("./info.txt", 'r')
            txt=info.read()
            self.img_and_price = ast.literal_eval(txt)
            info.close()
                
        except OSError and FileNotFoundError:
            pass

            
    def save_new_file(self,file_name,img):
        pass
    
    def exit_save(self):
        pass
    
    def save(self):
        info=open("./info.txt", 'w')
        info.write(str(self.img_and_price))
        info.close()
