class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lista=s.split()
        return len(lista[len(lista)-1])
        