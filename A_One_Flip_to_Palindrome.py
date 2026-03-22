t=int(input())
for _ in range(t):
    size=int(input())
    s=input()
    arr=[]
    for i in s:
        arr.append(int(i))
    print(arr)
    for i in range(size):
        p=arr.copy()
        print("rightside")
        for j in range(size-i):
            p[j]+=1
            p[j]%=2
        l=0
        r=size-1
        palindrome=True
        while(r>l):
            if p[l]!=p[r]:
                palindrome="False"
                break
            l+=1
            r-=1
        if palindrome:
            print(i,size-i,s,"is palindrome")

            
    
    
    
    