def to_dict(st):
    lis=list(st)
    di={}
    for x in lis:
        c=0
        for y in st:
            if x==y:
                c=c+1
               
        
        di[x]=c
    return di
        

print(to_dict("helloWorld"))

