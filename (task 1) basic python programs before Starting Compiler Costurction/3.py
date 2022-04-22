data={
    "NAME":["Shaheer","Ali","Ahmad","yolo"],
    "AGE":[22,21,20,23],
}
for x in data:
    print(x ,end="\t\t")
print("\n-------------------")
l=range(len(data))
data=data.values()
data=list(data)
for x in range(len(data[0])):
    
    for y in range(len(data)):
        print(data[y][x],end="\t\t")
    print("")