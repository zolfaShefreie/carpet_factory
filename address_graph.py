import math
import ast

class address_graph:
    
    def __init__(self,fac_nodes=[],instersection=[],edges=[]):
        self.fac_nodes=fac_nodes
        self.inst_nodes=instersection
        "for the edge that doesn't exist between two now , the value is 0"
        self.edges=edges
        
    def save(self):
        address=open("./address.txt", 'w')
        str_class=str(self.fac_nodes)+'\n'+str(self.inst_nodes)
        str_class+='\n'+str(self.edges)
        address.write(str_class)
        address.close()
    
    def load(self):
        try:
            address=open("./address.txt", 'r')
            count=0
            for line in address:
                line = ast.literal_eval(line)
                count+=1
                if count==1:
                    self.fac_nodes=line
                elif count==2:
                    self.inst_nodes=line
                elif count==3:
                    self.edges=line
            
            address.close()
                
        except OSError and FileNotFoundError:
            pass
        
    
    def nearest_factory(self, middleNode, length, node, nodes):
        length_factory=length[len(self.inst_nodes):]
        min=math.inf
        for i in range(0,length_factory):
            if length_factory[i]!=0 and length_factory[i]<min:
                min=length_factory[i]
                
        index=length.index(min)
        path_of_neareast_factory=[]
        path_of_neareast_factory.append(node)
        while True:
            middle=middleNode[index]
            if middle!=-1 and middle!=0:
                path_of_neareast_factory.insert(1,nodes[middle])
                index=middle
            else:
                break
        
        path_of_neareast_factory.append(nodes[length.index(min)])
        return {min:path_of_neareast_factory}
            
            
    
    def shortest_path(self,node):
        "dijsktra algorithm"
        if node not in self.inst_nodes and node not in self.fac_nodes:
            raise Exception("it doesn't exist")
        
        if node in self.fac_nodes:
            return {}
        
        nodes=self.inst_nodes+self.fac_nodes
        

        middleNode=[]
        length=[]
        visit_node=[]
        index=nodes.index(node)
        vnear=-1
        

        
        for i in range(0,len(nodes)):
            if i==index:
                middleNode.append(-1)
                length.append(-1)
                continue
            middleNode.append(index)
            length.append(self.edges[index][i])
        
        while len(visit_node)<len(nodes):
            min=math.inf
            for i in range(0,len(nodes)):
                if i==index:
                    continue
                if length[i]>0 and length[i]<min:
                    min=length[i]
                    vnear=i
            
            visit_node.append(vnear)
            for i in range(0,len(nodes)):
                if i==index or i in visit_node:
                    continue
                if length[vnear]+self.edges[vnear][i]<length[i]:
                    length[i]=length[vnear]+self.edges[vnear][i]
                    middleNode[i]=vnear
        
        path=self.nearest_factory(middleNode, length, node, nodes)
        
        return path
                
    def edges_list(self):
        "change to edge of networkx"
        i=0
        main_list=[]
        nodes=self.inst_nodes+self.fac_nodes
        for i  in range(0,len(nodes)):
            for j in range(0,len(nodes)):
                if self.edges[i][j]==0:
                    continue
                else:
                    t=(nodes[i],nodes[j],self.edges[i][j])
                    t1=(nodes[j],nodes[i],self.edges[i][j])
                if t not in main_list and t1 not in main_list:
                    main_list.append(t)
        
        return main_list
                    
    def is_empty(self):
        if len(self.fac_nodes)==0 or len(self.fac_nodes)==0:
            return True 
        return False
    
    def convert(self,dic_edget={}):
        list_ed=dic_edget[next(iter(dic_edget))]
        nodes=self.inst_nodes+self.fac_nodes
        return_list=[]
        for i in range(0,len(list_ed)-1):
            ed=self.edges[nodes.index(list_ed[i])][nodes.index(list_ed[i+1])]
            return_list.append((list_ed[i],list_ed[i],ed))
            
        return return_list
            
        
                
                
                