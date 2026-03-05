class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = []
        for i in points:
            l.append(i[0])
        l.sort()
        answer = 0
        for i in range(0, len(l) - 1):
            if answer < (l[i + 1] - l[i]):
                answer = l[i + 1] - l[i]

        return answer
