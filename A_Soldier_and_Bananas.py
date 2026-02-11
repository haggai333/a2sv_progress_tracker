lists=list(map(int,input().split()))
totalamount=0
for i in range(1,lists[2]+1):
    totalamount+=lists[0]*i
result=totalamount-lists[1]
if result>0:
    print(result)
else:
    print(0)
