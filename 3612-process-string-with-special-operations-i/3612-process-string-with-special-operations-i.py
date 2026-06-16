class Solution(object):
    def processStr(self, s):
        def reverse(l,r):
            if r<=l:
                return
            answer[l],answer[r]=answer[r],answer[l]
            reverse(l+1,r-1)
        answer=[]
        for i in s:
            if i=="#":
                answer+=answer
            elif i=="%":
                reverse(0,len(answer)-1)
            elif i=="*":
                if answer:
                    answer.pop()
            else:
                answer.append(i)
        return "".join(answer)
        