file=open("q1.txt","r")
lines=file.readlines()
file.close()
lines=[ x.replace("\n","").split('\t') for x in lines]
print(lines)
ip=input("input: ")
ip=list(ip)
states=("0","3")
s_state=states[0] #start state
e_state=states[1] #final state
for x in ip:
    print("current state: ",s_state)
    print("input processing: ",x)
    for y in lines:
        if(y[0]==s_state and y[1]==x):
            s_state=y[2]
            print("Next State: ",s_state)
            print("...")
            break
print("string accepted!" if (s_state==e_state) else "string rejected!")