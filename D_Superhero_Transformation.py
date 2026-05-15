s=input()
t=input()
if len(s)!=len(t):
    print("No")
else:
    a=set("aeiou")
    k=set(['w', 'k', 'd', 's', 'c', 'j', 'f', 'g', 'x', 'l', 'b', 'n', 'z', 'm', 'r', 'p', 'q', 'y', 't', 'h', 'v'])
    answer=True
    for i in range(len(s)):
        if s[i] in a and t[i] in a:
            continue
        if s[i] in k and t[i] in k:
            continue
        answer=False
        break
    
    if answer:
        print("Yes")
    else:
        print("No")