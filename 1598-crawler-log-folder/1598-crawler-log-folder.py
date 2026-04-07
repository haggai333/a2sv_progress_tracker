class Solution(object):
    def minOperations(self, logs):
        answer=0
        for i in logs:
            if i=="../":
                if answer>0:
                    answer-=1
            elif i=="./":
                continue
            else:
                answer+=1
        return answer
        