#The first line of each test case contains an integer n(1≤n≤105) — the number of members of the group excluding Alex.
#The second line contains nintegers a1,a2,…,an(1≤ai≤n) — the list of IDs of the members, sorted by decreasing times of last seen online at 9:00.
t=int(input())
for i in range(t):
    size=int(input())
    nomem=list(map(int,input().split()))
    ids=list(map(int,input().split()))
    n={}
    count=0
    l=len(nomem)-1
    r=len(ids)-1
    while l>=0 and r>=0:
        if nomem[l]>ids[r]:
            count+=1
            l-=1
        else:
            l-=1

        r-=1
    print(count)
        
