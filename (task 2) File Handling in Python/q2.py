seprators=['“ “',";" ,"=", "==", "(",")","{" ,"}"] 

file = open("q2.txt","r")
while(True):
    ch=file.read(1)
    if not ch:
        break
    if ch in seprators:
        print(ch, "this is a seprator")
    elif ch=="\n":
        continue
    else:
        print(ch)
file.close()