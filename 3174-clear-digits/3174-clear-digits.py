class Solution:
    def clearDigits(self, s: str) -> str:
        a=deque()
        for i in s:
            if i.isdigit():
                if a[-1].isalpha():
                    a.pop()
                continue
            a.append(i)
        return "".join(list(a))
        