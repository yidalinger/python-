# a="k:1|k3:2|k2:9"
# print(dict([tuple(i.split(':')) for i in a.split("|")]))

# li1=[1,1,1,2,3,4,4,4,5,6,5,7]
# d={}
# for i in li1:
#     d[i]=0
# print(d.keys())

# list = [1, 3, 6, 9, 1, 8,1,2,1]
# for x in list:
#     y=list.count(x)
#     if y>1:
#         list.remove(x)
# print(list)

# li1=[1,1,1,2,3,4,4,4,5,6,5,7,1,1,2]
# for i in li1:
#     a=li1.count(i)
#     print(i)
#     if a>1:
#         a=a-1
#         for j in range(a):
#             li1.remove(i)
# print(li1)
l1 = [2, 6, 9, 10, 18, 15, 1,8,7,88,21]
for i in range(len(l1)):
    for j in range(len(l1)-1):
        if l1[j]>l1[j+1]:
            l1[j] ,l1[j + 1]=l1[j+1] ,l1[j]
print(l1)
