n,m=map(int,input().split())
answers=list()
for _ in range(n):
    answers.append(input())
grading=list(map(int,input().split()))
total=0
for i in range(m):
    counts=[0]*5
    for j in range(n):
        counts[ord(answers[j][i])-ord("A")]+=1
    total+=max(counts)*grading[i]
print(total)
