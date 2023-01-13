def read_fsa_table(filename_list):
    all_fsa_table=[]
    all_fsa_char=[] 
    for x in filename_list:
        file=open(x,"r")
        lines=file.readlines()
        file.close()
        lines=[ x.replace("\n","").split('\t') for x in lines]
        characters={ x[1] for x in lines}
        all_fsa_table.append(lines)
        all_fsa_char.append(characters)
    return all_fsa_table,all_fsa_char

def read_input(filename):
    file=open(filename)
    data=file.readline()
    file.close()
    return data.split()

def LexicalAnalyzer(all_lines,all_characters,input_list,e_states ,s_state):
    tokens=[]
    operators={"=",'+','-',"*","&","!","|","~","<",">",'^',"[","]",":"}
    double_operators={"::",'[]','++',"--","<=",">=","!=","^=","%=",'*=',"-=","+=","&&","||",">>","<<","?:"}
    triple_operators={">>=",'===',"<<="}
    keywords=['alignas', 'decltype', 'namespace', 'struct', 'alignof', 'default', 'new', 'switch', 'and', 'delete', 'noexcept', 'template', 'and_eq', 'do', 'not', 'this', 'asm', 'double', 'not_eq', 'thread_local', 'auto', 'dynamic_cast', 'nullptr', 'throw', 'bitand', 'else', 'operator', 'true', 'bitor', 'enum', 'or', 'try', 'bool', 'explicit', 'or_eq', 'typedef', 'break', 'export', 'private', 'typeid', 'case', 'extern', 'protected', 'typename', 'catch', 'false', 'public', 'union', 'char', 'float', 'register', 'unsigned', 'char16_t', 'for', 'reinterpret_cast', 'using', 'char32_t', 'friend', 'return', 'virtual', 'class', 'goto', 'short', 'void', 'compl', 'if', 'signed', 'volatile', 'const', 'inline', 'sizeof', 'wchar_t', 'constexpr', 'int', 'static', 'while', 'const_cast', 'long', 'static_assert', 'xor', 'continue', 'mutable', 'static_cast', 'xor_eq']
    fsa_acceptance=[]
    for j in input_list:
        print("Processing String: ",j)
        ip_len=len(j)
        input_lexeme_list=list(j)
        current_states=[{"0"}]
        fsa_acceptance=[ True for x in range(len(all_lines))]
        operator_flag=False
        for index,char in enumerate(input_lexeme_list):
            if operator_flag:                                  
                operator_flag=False
            if char in operators:
                if  ip_len ==1:
                    if j in operators:
                         print(f"~~~~~~~~~~~~~~~~~~~  operator: {j}  ~~~~~~~~~~~~~~~~~~~")
                         operator_flag=True
                         tokens.append(j)
                         break
                    else:
                        print(f"!!!!!!!!!!!!!!!!!  Invalid Operator: {j}  !!!!!!!!!!!!!!!!!")
                        break
                elif ip_len==2:
                    if j in double_operators:
                         print(f"~~~~~~~~~~~~~~~~~~~  operator: {j}  ~~~~~~~~~~~~~~~~~~~")
                         operator_flag=True
                         tokens.append(j[0])
                         tokens.append(j[1])
                         break
                    else:
                        print(f"~~~~~~~~~~~~~~~~~~~  Invalid Operator: {j}  ~~~~~~~~~~~~~~~~~~~")
                        break
                elif ip_len==3:
                    if j in triple_operators:
                         print(f"~~~~~~~~~~~~~~~~~~~  operator: {j}  ~~~~~~~~~~~~~~~~~~~")
                         operator_flag=True
                         tokens.append(j[0])
                         tokens.append(j[1])
                         tokens.append(j[2])
                         break
                    else:
                        print(f"~~~~~~~~~~~~~~~~~~~  Invalid Operator: {j}  ~~~~~~~~~~~~~~~~~~~")
                        break   
                else:
                    print(f"~~~~~~~~~~~~~~~~~~~  Invalid Operator: {j}  ~~~~~~~~~~~~~~~~~~~")
                    break

            for fsa in range(len(all_lines)):
                if char not in all_characters[fsa] :
                    fsa_acceptance[fsa]=False
                if fsa_acceptance[fsa]==False:
                    continue
                print(f"fsa{fsa+1} current state: ",current_states[fsa])
                print("input processing: ",char)
                next_states=set()
                for current_state in current_states[fsa]:
                    for y in all_lines[fsa]:
                        if(y[0]==current_state and y[1]==char):
                            next_states.add(y[2])
                print("next states: ", next_states,"\n...")
                current_states[fsa]=next_states
        if operator_flag==True:
            continue
        for i in range(len(all_lines)):
            if fsa_acceptance[i]==False:
                print(f"FSA {i+1} Invalid Character! String Rejected")
            else:
                isAccepted=False
                for x in current_states[i]:
                    if x in e_states[i]:
                        isAccepted=True
            
                        break
                if isAccepted:
                    print(f"~~~~~~~~~~~~~~~~~~FSA{i+1} string accepted!~~~~~~~~~~~~~~~~~~~")
                    if i==0: #integer FSA
                        tokens.append("i")
                    else:
                        tokens.append("i") 
                else:
                    print(f"~~~~~~~~~~~~~~~FSA{i+1} string rejected!~~~~~~~~~~~~~~~~~")
    return "".join(tokens) + "$"   

def BottomUpParser(TABLE,SYMBOL,RHS,LHS,RULES,INPUT):
    class NT:
        def __init__(self,symbol,place) -> None:
            self.symbol=symbol
            self.place=place
            # print(self.__str__())
    def __str__(self) -> str:
        return f"symbol: {self.symbol} \nplace: {self.place}"

    STACK=[]
    STACK.append(0)
    CURRENT_IP_INDEX=0
    while(True):
        try:
            print("STACK: ",STACK)
            row=STACK[-1]
            col=SYMBOL.index(INPUT[CURRENT_IP_INDEX])
            value=TABLE[row][col]

            if "S" in value:
                state_number=int(value[1:])
                STACK.append(INPUT[CURRENT_IP_INDEX])
                STACK.append(state_number)
                CURRENT_IP_INDEX+=1
            elif "R" in value:
                reduction_number=int(value[1:])
                place=RHS[reduction_number]
                rhs_len=len(place)
                rhs_len*=2
                for x in range(rhs_len):
                    STACK.pop()
                val=''
                if RULES[reduction_number].startswith("="):
                    val=RULES[reduction_number].split()
                    val=val[1]
                    # print("i.val : ",val)
                else:
                    print(RULES[reduction_number])
                STACK.append(NT(symbol=LHS[reduction_number],place=val))
                row=STACK[-2]
                obj=STACK[-1]
                col=SYMBOL.index(obj.symbol)
                value=TABLE[row][col]
                STACK.append(value)  
            elif "A" in value :
                if INPUT[CURRENT_IP_INDEX]=='$':
                    print("")
                    print(" ----------------------")
                    print("|  PARSING SUCCESSFUL  |")  
                    print(" ----------------------")   
                    break
                else:
                    print("string rejected")
                    break
        except:
            print("")
            print(" ----------------------")
            print("|  PARSING FAILED  |")  
            print(" ----------------------")  
            break

        
def main():
    TABLE=[
    [-1,-1,'S4',-1,"S5",-1,-1,1,2,3],
    ["S6",-1,-1,-1,-1,"Accept",-1,-1,-1,-1],
    ["R2","S7",-1,"R2",-1,"R2",-1,-1,-1,-1],
    ["R4","R4",-1,"R4",-1,"R4",-1,-1,-1,-1],
    [-1,-1,"S4",-1,"S5",-1,-1,8,2,3],
    ["R6","R6",-1,"R6",-1,"R6",-1,-1,-1,-1],
    [-1,-1,"S4",-1,"S5",-1,-1,-1,9,3],
    [-1,-1,"S4",-1,"S5",-1,-1,-1,-1,10],
    ["S6",-1,-1,"S11",-1,-1,-1,-1,-1,-1],
    ["R1","S7",-1,"R1",-1,"R1",-1,-1,-1,-1],
    ["R3","R3",-1,"R3",-1,"R3",-1,-1,-1,-1],
    ["R5","R5",-1,"R5",-1,"R5",-1,-1,-1,-1],
    
]
    SYMBOL=['+','*','(',')','i','$','S','E','T','F']
    RHS=["E",'E+T','T','T*F','F','(E)','i']
    LHS=["S",'E','E','T','T','F','F']
    RULES=["At last Accepted","T is reduced","E+T is reduced","F is reduced","T*F is reduced","(E) is reduced","= xyz"]

    files=["identifier.txt"]
    all_lines,all_characters=read_fsa_table(files)
    end_states=[["1"]]
    start_states=[{"0"}]

    #INPUT="shaheer  8787 === sdfhgshd * shdfgsh"
    INPUT="abc + xyz"
    INPUT=INPUT.split()
    input_list=INPUT

    TOKENS=LexicalAnalyzer(all_lines,all_characters,input_list,end_states,start_states)

    print("")
    print(" ----------------------")
    print("|  TOKENS: ",TOKENS,"  |")  
    print(" ----------------------")

    BottomUpParser(TABLE,SYMBOL,RHS,LHS,RULES,TOKENS)
    

if __name__ == '__main__':
    main()
