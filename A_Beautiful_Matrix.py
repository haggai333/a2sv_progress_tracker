matrix=[]
for i in range(5):
    matrix.append(list(map(int,input().split())))
row=1
colum=1
for i in matrix:
    if 1 in i:
        colum=i.index(1)+1
        break
    colum+=1
    row+=1
print(abs(colum-3)+abs(row-3))