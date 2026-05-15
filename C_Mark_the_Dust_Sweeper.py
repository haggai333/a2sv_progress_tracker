t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    answer = 0
    ptr = 0
    while ptr < n and a[ptr] == 0:
        ptr += 1
    for i in range(ptr, n - 1):
        answer += a[i]
        if a[i] == 0:
            answer += 1
    print(answer)


