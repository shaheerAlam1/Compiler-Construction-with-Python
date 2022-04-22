def to_nested_dic(l1,l2,l3):
    return{ l1[x]:{l2[x]:l3[x]} for x in range(len(l1))}

        
l1=['S001', 'S002', 'S003', 'S004']
l2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3=[85, 98, 89, 92]

print(to_nested_dic(l1=l1,l2=l2,l3=l3))