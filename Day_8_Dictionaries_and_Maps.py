# Enter your code here. Read input from STDIN. Print output to STDOUT
a={}
size=int(input())
for i in range(size):
    thelist=input().split()
    a[thelist[0]]=thelist[1]
phoneBook=[]
for j in range(size):
    phoneBook.append(input())
for i in phoneBook:
    if i in a:
        print(i+'='+a[i])
    else:
        print("Not found")
        