def diff(lis1,lis2):
    print(lis1 ,"-", lis2)
    l=list(lis1)
    for x in l:
        if x in lis2:
            lis1.remove(x)
            lis2.remove(x)
    print(lis1+lis2)


lis1=[25,60,50,14,20]
lis2=[60,14,19]

diff(lis1,lis2)


