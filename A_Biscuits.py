numberoftest=int(input())
for i in range(numberoftest):
    nocokies=int(input())
    if nocokies<3:
        print(0)
        continue
    if nocokies%2==0:
        print(int((nocokies/2)-1))
    else:
        print(nocokies//2)