import factory_info_action
import sale_service
import os

class dataBase:
    img_path=[]
    address_path=[]
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
        add_dir=os.path.join(path,"address")
        if add_dir in os.listdir(path):
            for each in os.listdir(add_dir):
                new_path=path+"/"+str(each)
                self.address_path.append(new_path)
        else:
            try:
                os.mkdir(add_dir)
            except OSError:
                pass
            
    def save_new_file(self,file_name,imgOradd):
        pass
    
    def exit_save(self):
        pass
