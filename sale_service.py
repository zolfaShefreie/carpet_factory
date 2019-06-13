
class sale_service:

    def __init__(self):
        pass
    
    
    def two_d_to_1d(self,matrix=[[0]]):
        return_matrix=[]
        for i in range(0,len(matrix)):
            for each in matrix[i]:
                return_matrix.append(each)
                
        return return_matrix
                
    
    def min_penalty(self,matrix_base=[['0']],matrix_sec=[['0']]):
        matrix_base=self.two_d_to_1d(matrix_base)
        matrix_sec=self.two_d_to_1d(matrix_sec)
        len_base=len(matrix_base)
        len_sec=len(matrix_sec)
        
        list_alaki=[0 for i in range(0,len_base+1)]
        opt=[list_alaki for i in range(0,len_sec+1)]
        
        opt[len_sec][len_base]=0
        
        index=len_base-1
        j=1
        while index >= 0:
            opt[len_sec][index]=j*2
            index-=1
            j+=1
            
            
        index=len_sec-1
        j=1
        while index>=0:
            opt[index][len_base]=j*2
            index-=1
            j+=1
        
        for i in range(len_sec-1,-1,-1):
            for j in range(len_base-1,-1,-1):
                if matrix_base[i]==matrix_sec[j]:
                    penalty=0
                else :
                    penalty=1
                opt[i][j]=min(opt[i+1][j+1]+penalty,opt[i][j+1]+2,opt[i+1][j]+2)
                
        return opt[0][0]
                   
        
        


    # this function finds the maximum number of carpets that can be purchased with a certain amount of money that user enters

    def maximum_carpets(self,money,carpets_dic):
        prices=[]
        for each in carpets_dic.values():
            prices.append(each[0])
        carpets_id=[]
        for each in carpets_dic.keys():
            carpets_id.append(each)

        n=len(carpets_dic)

        # k this is the matrix that we fill to get the result
        k=[[0 for x in range(money+1)] for x in range(n+1)]

        for i in range(n+1):
            for p in range(money+1):
                if i==0 or p==0:
                    k[i][p]=0
                elif prices[i-1]<=p:
                    k[i][p]=max(1+k[i-1][p-prices[i-1]],k[i-1][p])
                else:
                    k[i][p]=k[i-1][p]

        max_number=k[n][money]
        bought_carpets=[]
        p=money
        for i in range(n,0,-1):
            if max_number<=0:
                break
            if max_number==k[i-1][p]:
                continue
            else:
                bought_carpets.append(carpets_id[i-1])
                max_number=max_number-1
                p=p-prices[i-1]

        return k[n][money],bought_carpets




