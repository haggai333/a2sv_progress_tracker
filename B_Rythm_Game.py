def solve():
    n, k = map(int, input().split())
    s = input()

    protection_count = 0

    for i in range(n):
        if s[i] == '1':
            has_previous_one = False

            for j in range(max(0, i - k + 1), i):
                if s[j] == '1':
                    has_previous_one = True
                    break

            if not has_previous_one:
                protection_count += 1

    return protection_count


t = int(input())
for _ in range(t):
    print(solve())