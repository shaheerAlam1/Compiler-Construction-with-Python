def read_ip():
    file=open("input.txt")
    data=file.readline()
    file.close()
    return data.split()

file=open("fsa.txt","r")
lines=file.readlines()
file.close()
lines=[ x.replace("\n","").split('\t') for x in lines]
characters={ x[1] for x in lines}
print(characters)
print(lines)
ip=read_ip()
for j in ip:
    print("Processing String: ",j)
    inp=list(j)
    states=("a","b")
    s_state=states[0]
    e_state=states[1]
    for x in inp:
        print("current state: ",s_state)
        print("input processing: ",x)
        if x not in characters:
            print(f"~~~~~~~~~~Invalid input character found! : '{x}'  ~~~~~~~~~")
            s_state=None
            break
        else:
            for y in lines:
                if(y[0]==s_state and y[1]==x):
                    s_state=y[2]
                    print("Next State: ",s_state)
                    print("...")
                    break
    print("~~~~~~~~~~~~~~~~~~string accepted!~~~~~~~~~~~~~~~~~~~" if (s_state==e_state) else "~~~~~~~~~~~~~~~string rejected!~~~~~~~~~~~~~~~~~")