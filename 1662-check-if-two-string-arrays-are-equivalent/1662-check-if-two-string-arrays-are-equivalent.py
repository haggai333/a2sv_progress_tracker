class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        value1=""
        value2=""
        for i in word1:
            value1+=i
        for i in word2:
            value2+=i
        return value1==value2