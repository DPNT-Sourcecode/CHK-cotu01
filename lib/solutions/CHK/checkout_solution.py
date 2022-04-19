

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    SKU=['A','B','C','D','E']
    sku_dic={}
    skus=tuple(skus)
    for i in skus:
        if i not in SKU:
            return -1
        if i not in sku_dic:
            sku_dic[i]=1
        else:
            sku_dic[i]+=1
    if 'B' in sku_dic and 'E' in sku_dic:
        sku_dic['B']=max(0,sku_dic['B']-sku_dic['E']//2)
    value=0
    for i in sku_dic:
        if i=='C':
            value+=sku_dic[i]*20
        elif i=='D':
            value+=sku_dic[i]*15
        elif i=='A':
            value+=sku_dic[i]%3*50+sku_dic[i]//3*130
        elif i=='B':
            value+=sku_dic[i]%2*30+sku_dic[i]//2*45
        elif i=='E':
            value+=sku_dic[i]*40
    return value



