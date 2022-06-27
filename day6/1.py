n=1
def dh(c):
    if c==1:
        return 4*n
    else:
        return 1.25*dh(c-1)+1
while True:
    if dh(6)%1==0:
        print(dh(6))
        break
    else:
        n=n+1









