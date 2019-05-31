
import math
class info_func:
    picture_matrix=[]
    def __init__(self):
        pass
    def default_matrix_multiplication(self,matrix_a,matrix_b):# if the  matices are 2*2 
        matrix_c=[]                            #c: the result of 'a' and 'b' multiplication
        matrix_c.append([])
        matrix_c.append([])
        matrix_c[0].append(matrix_a[0][0]*matrix_b[0][0]+matrix_a[0][1]*matrix_b[1][0])
        matrix_c[0].append(matrix_a[0][0]*matrix_b[0][1]+matrix_a[0][1]*matrix_b[1][1])
        
        matrix_c[1].append(matrix_a[1][0]*matrix_b[0][0]+matrix_a[1][1]*matrix_b[1][0])
        matrix_c[1].append(matrix_a[1][0]*matrix_b[0][1]+matrix_a[1][1]*matrix_b[1][1])
        
        return matrix_c
    
    def add(self,matrix_a,matrix_b): #addition of two matrices
        matrix_c=[]
        for i in range(0,len(matrix_a)):
            matrix_c.append([])
        for i in range(0,len(matrix_a)):
            for j in range(0,len(matrix_a)):
                matrix_c[i].append(matrix_a[i][j]+matrix_b[i][j])
        return matrix_c
    
    def sub(self,matrix_a,matrix_b): # subtraction of two matrices
        matrix_c=[]
        for i in range(0,len(matrix_a)):
            matrix_c.append([])
        for i in range(0,len(matrix_a)):
            for j in range(0,len(matrix_a)):
                matrix_c.append(matrix_a[i][j]-matrix_b[i][j])
                
        return matrix_c
    
    def split_matrix(matrix_a): #divide the matrix into four submatrices
        mid=len(matrix_a)//2
        c1=[]
        for i in range(0,mid):
            c1.append([])
            for j in range(0,mid):
                c1[i].append(matrix_a[i][j])
                
        c2=[]
        k=0
        for i in range(mid,len(matrix_a)):
            c2.append([])
            for j in range(0,mid):
                c2[k].append(matrix_a[i][j])
            k+=1
            
        c3=[]
        k=0
        for i in range(0,mid):
            c3.append([])
            for j in range(mid,len(matrix_a)):
                c3[k].append(matrix_a[i][j])
            k+=1
            
            
        c4=[]
        k=0
        for i in range(mid,len(matrix_a)):
            c4.append([])
            for j in range(mid,len(matrix_a)):
                c4[k].append(matrix_a[i][j])
            k+=1
            
        return c1,c3,c2,c4
    
    def strassen(self,matrix_a,matrix_b):
        if len(matrix_a)==2:
            return info_func.default_matrix_multiplication(matrix_a,matrix_b)
        A, B, C, D = info_func.split_matrix(matrix_a)
        E, F, G, H = info_func.split_matrix(matrix_b)
        
        p1 = info_func.strassen(A, info_func.sub(F, H))
        p2 = info_func.strassen(info_func.add(A, B), H)
        p3 = info_func.strassen(info_func.add(C, D), E)
        p4 = info_func.strassen(D, info_func.sub(G, E))
        p5 = info_func.strassen(info_func.add(A, D), info_func.add(E, H))
        p6 = info_func.strassen(info_func.sub(B, D), info_func.add(G, H))
        p7 = info_func.strassen(info_func.sub(A, C), info_func.add(E, F))
        
        top_left = info_func.add(info_func.sub(info_func.add(p5, p4), p2), p6)
        top_right = info_func.add(p1, p2)
        bot_left = info_func.add(p3, p4)
        bot_right = info_func.sub(info_func.sub(info_func.add(p1, p5), p3), p7)
        
        # construct the new matrix from our 4 quadrants
        new_matrix = []
        for i in range(len(top_right)):
            new_matrix.append(top_left[i] + top_right[i])
        for i in range(len(bot_right)):
            new_matrix.append(bot_left[i] + bot_right[i])
        return new_matrix
        
    
    def strassen_multiplication(self,matrix_b):  #matrix_b is the matrix that user inters
        matrix_a=info_func.picture_matrix  #matrix_a is the picture_matrix
        
        a_rows=len(matrix_a)  # number of rows of picture_matrix
        a_columns=len(matrix_a[0])    #number of columns of picture_matrix
        
        #the dimensions of picture_matrix must be a number of power 2
        
        if a_rows>a_columns:
            if isinstance(math.log(a_rows,2),float)==True:
                n=math.ceil(math.log(a_rows,2))  #the nearest power of 2 to the current dimension
                
                for i in range(0,a_rows):
                    for j in range(a_columns,2**n):
                        matrix_a[i].append(0)
                        
                for i in range(a_rows,2**n):
                    matrix_a.append([])
                    for j in range(0,2**n):
                        matrix_a[i].append(0)
                        
            else:
                n=math.log(a_rows,2)
                for i in range(0,a_rows):
                    for j in range(a_columns,2**n):
                        matrix_a[i].append(0)
                        
        else:
            if isinstance(math.log(a_columns,2),float)==True:
                n=math.ceil(math.log(a_columns,2))
                for i in range(0,a_rows):
                    for j in range(a_columns,2**n):
                        matrix_a[i].append(0)
                        
                for i in range(a_rows,2**n):
                    matrix_a.append([])
                    for j in range(0,2**n):
                        matrix_a[i].append(0)
                        
            else:
                n=math.log(a_columns,2)
                for i in range(a_rows,2**n):
                    matrix_a.append([])
                    for j in range(0,2**n):
                        matrix_a[i].append(0)
                        
                        
        b_rows=len(matrix_b)
        b_columns=len(matrix_b[0])
        
        if b_rows<len(matrix_a) and b_columns<len(matrix_a):
            for i in range(b_rows,len(matrix_a)):
                matrix_b.append([])
                for j in range(0,len(matrix_a)):
                    matrix_b[i].append(0)
                    
            for i in range(0,b_rows):
                for j in range(b_columns,len(matrix_a)):
                    matrix_b[i].append(0)
                    
        if b_rows>len(matrix_a) and b_columns>len(matrix_a):
            for i in range(len(matrix_a),b_rows):
                matrix_b.pop()
            for i in range(0,len(matrix_a)):
                for j in range(len(matrix_a),b_columns):
                    matrix_b[i].pop()
                    
        if b_rows<len(matrix_a) and b_columns>len(matrix_a):
            for i in range(0,b_rows):
                for j in range(len(matrix_a),b_columns):
                    matrix_b[i].pop()
                    
            for i in range(b_rows,len(matrix_a)):
                matrix_b.append([])
                for j in range(0,len(matrix_a)):
                    matrix_b[i].append(0)
                    
        if b_rows>len(matrix_a) and b_columns<len(matrix_a):
            for i in range(len(matrix_a),b_rows):
                matrix_b.pop()
            for i in range(0,len(matrix_a)):
                for j in range(b_columns,len(matrix_a)):
                    matrix_b[i].append(0)
                    
        if b_rows>len(matrix_a) and b_columns==len(matrix_a):
            for i in range(len(matrix_a),b_rows):
                matrix_b.pop()
                
        if b_rows<len(matrix_a) and b_columns==len(matrix_a):
            for i in range(b_rows,len(matrix_a)):
                matrix_b.append([])
                for j in  range(0,len(matrix_a)):
                    matrix_b[i].append(0)
                    
        if b_columns<len(matrix_a) and b_rows==len(matrix_a):
            for i in range(0,len(matrix_a)):
                for j in range(b_columns,len(matrix_a)):
                    matrix_b[i].append(0)
                    
        if b_columns>len(matrix_a) and b_rows==len(matrix_a):
            for i in range(0,len(matrix_a)):
                for j in range(len(matrix_a),b_columns):
                    matrix_b[i].pop()
                    
        return info_func.strassen(matrix_a,matrix_b)
                    
        
                        
                
                
                
        
        
        
            
            
        
        
        
        
    

        