seprators=['“ “',";" ,"=", "==", "(",")","{" ,"}"] 

file = open("q2.txt","r")
file2=open("output.txt","w")

while(True):
    ch=file.read(1)
    if not ch:
        break
    if ch in seprators:
        file2.write( ch +"this is a seprator\n")
    elif ch=="\n":
        continue
    else:
        file2.write(ch+"\n")

file.close()
file2.close()