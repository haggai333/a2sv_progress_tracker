lists=list(map(int,input().split()))
totalamount=0
for i in range(1,lists[2]+1):
    totalamount+=lists[0]*i
print(totalamount-lists[1])

