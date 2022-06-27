# def fun(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fun(n - 1) + fun(n - 2)
# a = []
# for i in range(1, 11):
#     a.append(fun(i))
# print(a)

# a=[1,2,3,4,5,6,7,8,9,10]
# b=[i for i in a if i%2==1]
# print(b)
# a='http://ip:port/extername/get_account_trade_record.json?page_size=20&page_index=1&user_id=203317&trade_type=0'
# print(dict([tuple(i.split('=')) for i in a.split("?")[1].split('&')]))
a=2
b=3
c=a if (a>=b) else b
print(c)