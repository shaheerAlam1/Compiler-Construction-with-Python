INPUT=["i","+","i","*","i","$"]
TERMINALS=['i','+','*','$']
TABLE=[
    #i    +   *   $
    ['_','>','>','>'], #i
    ['<','>','<','>'], #+
    ['<','>','>','>'], #*
    ['<','<','<','_'], #$
]
STACK=[]
STACK.append("$")
def check_precedence(row,col):
    if TABLE[row][col] in ["_","<"]:
        return True #push
    else :
        return False #pop
LAST_INDEX=len(INPUT)-1


for index,ip in enumerate(INPUT):
    row = TERMINALS.index(STACK[-1])
    col= TERMINALS.index(ip)
    precedence=check_precedence(row,col)
    if precedence:
        STACK.append(ip)
    else:
        STACK.pop()
    if LAST_INDEX==index and  ip=="$" and STACK==[]:
        print("parsing successful")
    
    