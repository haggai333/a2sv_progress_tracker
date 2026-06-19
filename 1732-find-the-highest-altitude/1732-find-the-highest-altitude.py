class Solution(object):
    def largestAltitude(self, gain):
        answer=0
        sumi=0
        for i in gain:
            sumi+=i
            answer=max(sumi,answer)
        return answer
        