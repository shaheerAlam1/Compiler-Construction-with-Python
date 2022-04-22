dic={'Math':81, 'Physics':83, 'Chemistry':87}
print(sorted(dic.items(), key=lambda i: i[-1] ,reverse=True))
