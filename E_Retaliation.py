import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    d = a[1] - a[0]
    ok = True
    for i in range(1, n):
        if a[i] - a[i - 1] != d:
            ok = False
            break

    if not ok:
        print("NO")
        continue

   
    if (a[0] - d) % (n + 1) != 0:
        print("NO")
        continue

    y = (a[0] - d) // (n + 1)
    x = d + y

    
    if x >= 0 and y >= 0:
        print("YES")
    else:
        print("NO")