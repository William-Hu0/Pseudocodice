a=int(input())
b=a
while True:
    b-=1
    if b==0:
        break
    else:
        a*=b
print(a)