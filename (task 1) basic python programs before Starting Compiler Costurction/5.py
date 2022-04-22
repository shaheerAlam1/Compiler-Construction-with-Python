data={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
d2=dict(sorted(data.items(), key=lambda item: item[1],reverse=True))
c=0
for x, y in d2.items():
    if c==3:
        break
    print (x,"  ",y)
    c=c+1
