def checkout(skus):
    sku_dic={}
    skus=tuple(skus)
    for i in skus:
        if not(ord(i)-ord('A')>=0 and ord(i)-ord('A')<=25):
            return -1
        if i not in sku_dic:
            sku_dic[i]=1
        else:
            sku_dic[i]+=1
    #5A-200, 3A-130, 2EB-80, 2B-45, 3F-20, 10H-80, 5H-45, 2K-150,
    #3NM-120, 5P-200, 3Q-80, 3RQ-150, 4U-120, 3V-130, 2V-90
    #classified two types
    #2EB-80,3NM-120,3RQ-150,
    #5A-200, 3A-130, 2B-45, 3F-20, 10H-80, 5H-45, 2K-150,
    #5P-200, 3Q-80, 4U-120, 3V-130, 2V-90
    policy1=[(('E','B'),(2,1)),(('N','M'),(3,1)),(('R','Q'),(3,1))]
    policy2=[('A',5,200),('A',3,130),('B',2,45),('F',3,20),('H',10,80),('H',5,45),('K',2,120),('P',5,200),
             ('Q',3,80),('U',4,120),('V',3,130),('V',2,90)]
    price={'A':50,'B':30,'C':20,'D':15,'E':40,'F':10,'G':20,'H':10,'I':35,'J':60,'K':70,'L':90,'M':15,
           'N':40,'O':10,'P':50,'Q':30,'R':50,'S':20,'T':20,'U':40,'V':50,'W':20,'X':17,'Y':20,'Z':21}
    for i,j in policy1:
        if i[0] in sku_dic and i[1] in sku_dic: #i[0]-E,i[1]-B
            sku_dic[i[1]]=max(0,sku_dic[i[1]]-sku_dic[i[0]]//j[0])
    
    for i,j,k in policy2:
        if i in sku_dic:
            temp=sku_dic[i]
            sku_dic[i]=temp%j
            sku_dic[str(j)+i]=temp//j
            price[str(j)+i]=k
    policy3=[
        (3,[('S',20),('T',20),('X',17),('Y',20),('Z',21)],45)
    ]

    value=0
    for k,i,v in policy3:
        quantity=sum([sku_dic[j] for j in [x[0] for x in i]])
        left=quantity%k
        value+=quantity//k*v
        i.sort(key=lambda x:x[1])
        if left!=0:
            flag=0
        else:
            flag=1
        for j in i:
            if j[0] in sku_dic:
                if flag==1:
                    sku_dic[j[0]]=0
                    continue
                if sku_dic[j[0]]>=left:
                    sku_dic[j[0]]=left
                    flag=1
                else:
                    left-=sku_dic[j[0]]
                    sku_dic[j[0]]=0
                    flag=0
    for i in sku_dic:
        value+=price[i]*sku_dic[i]
    return value