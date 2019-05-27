import factory_info_action
import sale_service
import os

class dataBase:
    img_path=[]
    address_path=[]
    factory_func=factory_info_action.info_func()
    sale_func=sale_service.sale_service()
    def __init__(self):
        path="./img"
        for each in os.listdir(path):
            new_path=path+"/"+str(each)
            self.img_path.append(new_path)
        path="./address"
        for each in os.listdir(path):
            new_path=path+"/"+str(each)
            self.address_path.append(new_path)
            
    def save_new_file(self,file_name,imgOradd):
        pass
    
    def exit_save(self):
        pass
