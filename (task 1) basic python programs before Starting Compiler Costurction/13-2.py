lis=["a",'b','c']
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact = fact * num
    return(fact)

n=factorial(len(lis))
c=0
t=0
for x in range(n):
    if(t==2):
        c=c+1
        t=0

    for x in range(len(lis)):
        if x==c:
            continue
        else:
            print(lis[c],",",lis[x])
        
    print(c)
    t=t+1


# for x in range(len(lis)):


