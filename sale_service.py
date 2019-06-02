
class sale_service:
    
    result_grath_coloring=[]
    
    def __init__(self):
        pass
<<<<<<< HEAD
    
    def first_input(self,n):
        colors=[]
        for i in range(0,n):
            colors.append(0)
        
        return colors
    
    def promising(self,count=0,colors=[],edges=[]):
        switch = True
        j = 1;
        while j < count and switch:
            if edges[count][j] and colors[count] == colors[j]:
                switch=False
            j+=1
            
        return switch
            
    
    def grath_coloring(self,count=0,colors=[],edges=[],num_of_color=1): 
        if self.promising (count,colors,edges):
            if count == num_of_color:
                self.result_grath_coloring.appent(colors)
            else:
                for color in range(1,num_of_color+1):
                    colors[count + 1] = color
                    self.grath_coloring(count + 1,colors,edges,num_of_color)
                    
                    
    def min_color(self,num_of_color=1):
        # find min of max every result
        min = num_of_color
        for each in self.result_grath_coloring:
            max_each=max(each)
            if max_each < min:
                min = max_each
                
        return min

        
=======

    # this function finds the maximum number of carpets that can be purchased with a certain amount of money that user enters

    def maximum_carpets(self,money,carpets_dic):
        prices=[]
        for each in carpets_dic.values():
            prices.append(each)
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




        
>>>>>>> 5a80790deb9f549292c6587f74acfb4667a502d8
