
class sale_service:

    def __init__(self):
        pass


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




