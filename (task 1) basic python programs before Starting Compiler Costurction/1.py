def comb(data):
    data=list(data.values())
    c=0
    for x in range(len(data)):
        for y in range(len(data[1])):
            print(data[0][x],data[1][y])
data = {'1':['a','b'], '2':['c','d']}
comb(data)