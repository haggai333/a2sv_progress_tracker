n = int(input())

for _ in range(n):
    size = int(input())
    arrays = list(map(int, input().split()))
    arrays.sort()
    
    b = True
    j = 1
    
    while j < size:   
        if arrays[j] - arrays[j - 1] > 1:
            b = False
            break
        j += 1
            
    if b:
        print("YES")
    else:
        print("NO")