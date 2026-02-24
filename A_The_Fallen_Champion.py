w,t=list(map(int,input().split()))
n=int(input())
fallen=True
for i in range(n):
    wi,ti=list(map(int,input().split()))
    if wi>=w and t>ti:
        print("The Fallen Champion")
        fallen=False
        break
if fallen:
    print("The Champion Saves the Accused")
    

