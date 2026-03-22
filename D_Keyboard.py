t=int(input())
for _ in range(t):
    s=input()

    if len(s)==1:
        print(s)
        continue
    ss=list("abcdefghijklmnopqrstuvwxyz")
    alphabet=[]
    for i in range(26):
        alphabet.append([])
    
    counti=0
    checker=0
    current=s[0]
    for i in range(len(s)):
        if current==s[i]:
            counti+=1
        else:
            alphabet[ord(current)-ord('a')].append(counti)
            checker+=counti

            current=s[i]
            counti=1
        if i==len(s)-1:
            alphabet[ord(current)-ord('a')].append(counti)
            checker+=counti
    checker=checker//len(set(s))
    answer=set()
    for i in s:
        p=ord(i)-ord('a')
        if len(alphabet[p])==1:
            if  alphabet[p][0]!=checker:
                answer.add(ss[p])
                continue
        for j in range(1,len(alphabet[p])):
            if alphabet[p][j-1]!=alphabet[p][j]:
                answer.add(ss[p])
                continue
    answer=list(answer)
    answer.sort()
    print("".join(answer))


