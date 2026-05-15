t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    seen = set()
    mex = 0
    mx = 0
    ans = 0

    for x in arr:
        seen.add(x)
        while mex in seen:
            mex += 1
        mx = max(mx, x)
        ans += mex + mx

    print(ans)