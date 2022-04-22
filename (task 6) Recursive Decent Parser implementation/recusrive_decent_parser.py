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

def fsm_in_parallel(all_lines,all_characters,input_list,e_states ,s_state):
    lis=[]
    seprators={"=",'+','-',"*","&","!","|"}
    keywords=['alignas', 'decltype', 'namespace', 'struct', 'alignof', 'default', 'new', 'switch', 'and', 'delete', 'noexcept', 'template', 'and_eq', 'do', 'not', 'this', 'asm', 'double', 'not_eq', 'thread_local', 'auto', 'dynamic_cast', 'nullptr', 'throw', 'bitand', 'else', 'operator', 'true', 'bitor', 'enum', 'or', 'try', 'bool', 'explicit', 'or_eq', 'typedef', 'break', 'export', 'private', 'typeid', 'case', 'extern', 'protected', 'typename', 'catch', 'false', 'public', 'union', 'char', 'float', 'register', 'unsigned', 'char16_t', 'for', 'reinterpret_cast', 'using', 'char32_t', 'friend', 'return', 'virtual', 'class', 'goto', 'short', 'void', 'compl', 'if', 'signed', 'volatile', 'const', 'inline', 'sizeof', 'wchar_t', 'constexpr', 'int', 'static', 'while', 'const_cast', 'long', 'static_assert', 'xor', 'continue', 'mutable', 'static_cast', 'xor_eq']
    fsa_acceptance=[]
    for j in input_list:
        print("Processing String: ",j)
        input_lexeme_list=list(j)
        # s_state="0"
        current_states=s_state
        fsa_acceptance=[ True for x in range(len(all_lines))]
        seprator_flag=False
        for index,char in enumerate(input_lexeme_list):
            if seprator_flag:
                seprator_flag=False
            if char in seprators:
                try:
                    if input_lexeme_list[index+1] in seprators:
                        print(f"~~~~~~~~~~~~~~~~~~~  Seprator: {char}{input_lexeme_list[index+1]}  ~~~~~~~~~~~~~~~~~~~")
                        seprator_flag=True
                        lis.append(f"{char}{input_lexeme_list[index+1]}")
                        break
                    else:
                        print("~~~~~~~~~~~~~~~~~~~  Seprator:",char,"  ~~~~~~~~~~~~~~~~~~~")
                        lis.append(char)
                        seprator_flag=True
                        break
                except:
                    print("~~~~~~~~~~~~~~~~~~~  Seprator:",char,"  ~~~~~~~~~~~~~~~~~~~")
                    seprator_flag=True
                    lis.append(char)
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
        if seprator_flag==True:
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
                # if (i==1):
                #     if x in keywords and isAccepted==True:
                #         print(f"~~~~~~~~~~~~~~~~~~FSA{i+1} string accepted (indentifier)!~~~~~~~~~~~~~~~~~~~")
                if i==0 and isAccepted:
                    if j in keywords:
                        print(f"~~~~~~~~~~~~~~~~~~FSA {i+1}  Keyword! string accepted!~~~~~~~~~~~~~~~~~~~")
                        lis.append("k")
                    else:
                        print(f"~~~~~~~~~~~~~~~FSA{i+1}  It is an identifer~~~~~~~~~~~~~~~~~")
                        lis.append("i")
                    continue

                print(f"~~~~~~~~~~~~~~~~~~FSA{i+1} string accepted!~~~~~~~~~~~~~~~~~~~" if isAccepted else f"~~~~~~~~~~~~~~~FSA{i+1} string rejected!~~~~~~~~~~~~~~~~~")
    return lis


files=["identifier.txt","integer.txt"]
all_lines,all_characters=read_fsa_table(files)
input_list=read_input("input.txt")
end_states=[["1"],["1"]]
start_states=[{"0"},{"0"}]

data=fsm_in_parallel(all_lines,all_characters,input_list,end_states,start_states)

input=""
for x in data:
    if (x=="i" or x=="+"):
        input=input+x
input=input+"$"
print(input)
# input = "ii$" #$ is end of input,,
i=0
charc = input[i] # we will start with first charcter
rval = True # This is global flag to check whether parsing was succeed
# we are declaring input as global, so that it is accessable to all functions

# This function will match input charatcer with Grammar Charatcer
def match(var): # here charc point to the charcter, that need to be matched
    global i
    global input
    global charc
    global rval
    if(var == input[i] and var != "$"): 
        # if the charcter is matched with string charcter, but it should not be the end charcter
         i=i+1  # You need to go to next charcter
         charc =  input[i]
         rval = True
         return rval #Its Fine Go Ahead,,as no error is their
    else:
        #print("\n There is an Error in the input string")
        rval = False
        return rval  # It means their is an Error, You need to quite

def E(): #This function implemnts E non-terminal
    global i
    global input
    global charc
    global rval
    if( charc == "i"): 
        rval = match("i")
        if rval and charc !="$": #It means its True and we are not at end of input
            rval = E_bar()  # Then proceed further in parsing
        else:
            return rval
    else:
        return False
    return rval

def E_bar():
    global i
    global input
    global charc
    global rval
    if( charc == "+"): #if input is +, we also need to check next charcter
    # whether it is i or not ,,as production is E'--->+iE'
        rval = match("+")
        #rval = match("i")
        if rval: # then match next i
            rval = match("i")
            if rval and charc != "$": # we are not at end of input
                rval = E_bar()
            else:
                return rval
        else:
            return rval # return rvale 
        
    else:
        rval = False
        return rval # simply return to previous function in recusrrion
    return rval

if __name__ == "__main__": # This is the main Function 
    #global rval
    rval = E()
    if( rval): # we reached end of parsing, and still rval is True
        print("\n Parsing Succeed")
    else:
        print("\n There is an Error While Parsing")

