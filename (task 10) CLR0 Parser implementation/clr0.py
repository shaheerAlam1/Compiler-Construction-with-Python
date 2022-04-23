TABLE = [ 
    ['S3','S4',-1,1,2],
    [-1,-1,"Accept",-1,-1],
    ['S3','S4',-1,-1,5],
    ['S3','S4',-1,-1,6],
    ['R2','R2','R2',-1,-1],
    ['R0','R0','R0',-1,-1],
    ['R1','R1','R1',-1,-1],
 ]
SYMBOL=['a','b','$','S','A']
RHS=['AA','aA','b']
LHS=['S','A','A']
INPUT='aabb$'
STACK=[]
STACK.append(0)
CURRENT_IP_INDEX=0
while(True):
    print(STACK)
    row=STACK[-1]
    col=SYMBOL.index(INPUT[CURRENT_IP_INDEX])
    print("col:",col)
    print("row:",row)
    value=TABLE[row][col]
    print(value)
    if "S" in value:
        state_number=int(value[1])
        STACK.append(INPUT[CURRENT_IP_INDEX])
        STACK.append(state_number)
        CURRENT_IP_INDEX+=1
    elif "R" in value:
        reduction_number=int(value[1])
        rhs_len=len(RHS[reduction_number])
        rhs_len*=2
        for x in range(rhs_len):
            STACK.pop()
        STACK.append(LHS[reduction_number])
        row=STACK[-2]
        col=SYMBOL.index(STACK[-1])
        value=TABLE[row][col]
        STACK.append(value)  
    elif "A" in value :
        if INPUT[CURRENT_IP_INDEX]=='$':
            print("parsing successful")
            
            break
        else:
            print("string rejected")
            break

