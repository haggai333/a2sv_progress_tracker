def solve():
    n = int(input())
    u = list(map(int, input().split()))
    s = list(map(int, input().split()))

    groups = {}
    for i in range(n):
        if u[i] not in groups:
            groups[u[i]] = []
        groups[u[i]].append(s[i])


    all_group_data = []
    for g in groups:
        skills = sorted(groups[g], reverse=True)
        pref = [0] * (len(skills) + 1)

        for i in range(len(skills)):
            pref[i + 1] = pref[i] + skills[i]

        all_group_data.append(pref)

    
    ans = [0] * (n + 1)

    for pref in all_group_data:
        m = len(pref) - 1

        for k in range(1, m + 1):
            num = (m // k) * k
            ans[k] += pref[num]

    return " ".join(map(str, ans[1:]))



t = int(input())
for _ in range(t):
    print(solve())