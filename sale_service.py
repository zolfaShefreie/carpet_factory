
class sale_service:
    
    result_grath_coloring=[]
    
    def __init__(self):
        pass
    
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

        