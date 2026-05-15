arr=list("A2SV")
n=int(input())

def factorial(n):
    if n<1:
        return 0
    if n==1:
        return 1
    return n*factorial(n-1)


answer=n
k=1
for i in range(n-1,0,-1):
    k*=factorial(n)
answer-k
print(k)
      
      





