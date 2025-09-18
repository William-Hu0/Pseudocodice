a=int(input())
b=a
while True:
    b-=2
    a+=b
    if b==0:
        break
print(a)