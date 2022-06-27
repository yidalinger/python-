def jc(n):
    a = [1]
    for i in range(2,n+1):
        sum1 = 1
        for j in range(1,i+1):
            sum1 = sum1*j
        a.append(a[-1]+sum1)
    return a
print(jc(6))
