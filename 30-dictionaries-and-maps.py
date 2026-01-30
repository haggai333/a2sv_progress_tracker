# Enter your code here. Read input from STDIN. Print output to STDOUT
a={}
size=int(input())
for i in range(size):
    name,number=input().split()
    a[name]=number

while True:
        try:
            listcheck= input()
            if listcheck in a:
                print(f"{listcheck}={a[listcheck]}")
            else:
                print("Not found")
        except EOFError:
            break   
