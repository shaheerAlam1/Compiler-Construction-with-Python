TABLE = [
#    i    +    *   (    )    $
    [0 , -1 , -1 , 0 , -1 , -1], #E
    [-1 , 1 , -1 , -1 , 2 , 2], #P
    [3 , -1 , -1 , 3 , -1 , -1], #T
    [-1 , 5 , 4 , -1 , 5 , 5], #G
    [6 , -1 , -1 , 7 , 0 , 0], #F
]
EPSILON="!"
RULES = ["TP", "+TP", EPSILON, "FG", "*FG", EPSILON, "i", "(E)"]
INPUT=["i" , "+", "i","+","i", "$"]
NON_TERMINALS=["E", "P", "T", "G", "F"]
TERMINALS=['i', '+', "*", "(", ")", "$"]
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
        if production==EPSILON:
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

        
    
