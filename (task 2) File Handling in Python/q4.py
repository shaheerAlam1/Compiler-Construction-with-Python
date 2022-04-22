file=open("q4.txt","r")
lines=file.readlines()
lines=[ x.replace("\n","").split('\t') for x in lines]
print(lines)

ch=input("please enter a character: ")
no=int(input("please enter any number: "))
sett=set()

for x in lines:
    if(int(x[0])==no and x[1]==ch ):
        sett.add(x[2])
print(sett)
file.close()