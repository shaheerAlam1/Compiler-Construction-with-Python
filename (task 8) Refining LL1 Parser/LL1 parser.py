def read_table(filename):
    file=open(filename,"r")
    data=file.readlines()
    file.close()
    data=[ x.replace("\n","").split()   for x in data]
    table=[]
    for x in data:
        x=[ int(i) for i in x]
        table.append(x)
    return table

def read_file(filename):
    file=open(filename,"r")
    data=file.readline()
    file.close()
    return data.split()

EPISLON="!"
TABLE=read_table("table.txt")
RULES = read_file("production.txt")
INPUT=read_file("Input.txt")
NON_TERMINALS=read_file("Non_Terminal.txt")
TERMINALS=read_file("Terminal.txt")

stackk=[]
stackk.append('$')
stackk.append(NON_TERMINALS[0])
last_index=len(INPUT)-1
invalid_flag=False
for ip in INPUT:
    while ip!=stackk[-1] :
        row=NON_TERMINALS.index(stackk[-1])
        col=TERMINALS.index(ip)
        production=TABLE[row][col]
        if production==-1:
            print("invalid production")
            invalid_flag=True
            break
        production=RULES[production]
        if production==EPISLON:
            stackk.pop()
            print(stackk)
            continue
        production_list=list(production)
        production_list.reverse()
        stackk.pop()
        print(stackk)
        for x in production_list:
            stackk.append(x)
        print(stackk)
    if invalid_flag==True:
        break
    if ip=="$" and stackk[-1]=="$":
        print("parsing successfull")
    stackk.pop()

        
    
