def matching(lis):
    l=list(lis)
    c=0
    for x in lis:
        if len(x)<2:
            l.remove(x)
            continue
        if x[0]==x[-1]:
            c=c+1
    return(c)

print(matching(["hello","ho","aba","bulb"]))