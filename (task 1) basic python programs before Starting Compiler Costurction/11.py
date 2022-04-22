def sortit(tuples):
    return sorted(tuples, key=lambda i:i[-1])  
lis=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sortit(lis))