def solve():
    n, c, d = map(int, input().split())

    b = list(map(int, input().split()))

    a11 = min(b)

    expected = []
    for i in range(n):
        for j in range(n):
            expected.append(a11 + i * c + j * d)

    if sorted(b) == sorted(expected):
        return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    print(solve())