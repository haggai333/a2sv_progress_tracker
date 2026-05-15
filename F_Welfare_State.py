n = int(input())
nums = list(map(int, input().split()))
q = int(input())
queries = []
for _ in range(q):
    temp = list(map(int, input().split()))
    queries.append(temp)

maxx = 0
flag = [False] * n  

for i in range(q - 1, -1, -1):
    if queries[i][0] == 2:
        maxx = max(maxx, queries[i][1])
    else:
        idx = queries[i][1] - 1
        x = queries[i][2]
        if not flag[idx]:
            nums[idx] = max(x, maxx)
            flag[idx] = True

for i in range(n):
    if not flag[i]:
        nums[i] = max(nums[i], maxx)

print(*nums)




