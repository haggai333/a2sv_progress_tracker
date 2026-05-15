import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input().strip()

    if c == 'g':
        print(0)
        continue
    next_g = [-1] * (2 * n)

    last = -1
    for i in range(2 * n - 1, -1, -1):
        if s[i % n] == 'g':
            last = i
        next_g[i] = last

    ans = 0

    for i in range(n):
        if s[i] == c:
            ans = max(ans, next_g[i] - i)

    print(ans)