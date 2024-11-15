n=int(input())
num=1
for i in range(1, n+1):
    print(*range(num,num+i))
    num += i
