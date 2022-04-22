file= open("q1.txt","r")
lines=file.readlines()
data=[  x.replace("\n","").split("\t")  for x in lines]
print(data)
file.close()
