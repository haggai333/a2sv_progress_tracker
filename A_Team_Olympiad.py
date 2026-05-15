size=int(input())
arr=list(map(int,input().split()))
checker=[[],[],[]]
for i,val in enumerate(arr):
    checker[val-1].append(i+1)
teams=[]
size=float("inf")
for i in checker:
    size=min(size,len(i))
print(size)
for i in range(size):
    print(*[checker[0][i],checker[1][i],checker[2][i]])