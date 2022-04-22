def permute(data):
    data=list(data)
    print(data)
    print(len(data))
    p=[]
    for x in range(len(data)-1):
        tp=[data[x]]
        for y in range(x+1,len(data)):   
            tp.append(data[y])
        p.append(tp)
    return p

data="abcdef"
print(permute(data))