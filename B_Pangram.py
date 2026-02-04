n=int(input())
stringval=input()
setval=set()
for i in stringval:
    setval.add(i.lower())
    
if(len(setval))!=26:
    print("NO")
   
else:
    print("YES")