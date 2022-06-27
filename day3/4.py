a =['a','b','c','d','e']
b =[1,2,3,4,5]
# c={}
# for i in range(len(a)):
#     # c[a[i]]=b[i]
#     # c.setdefault(a[i],b[i])
#     c.update({a[i]:b[i]})
# print(c)
# d=[([a[i],b[i]]) for i in range(len(a))]
# print(dict([([a[i],b[i]]) for i in range(len(a))]))
d=list(zip(a,b))
print(d)









# c={}
# for i in range(len(a)):
#     c[a[i]]=b[i]
#     # c.setdefault(a[i],b[i])
#     # c.update({a[i]:b[i]})
# print(c)