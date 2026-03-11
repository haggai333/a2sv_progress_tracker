class Solution(object):
    def countVowelSubstrings(self, word):
        a=set("aeiou")
        count=0
        for i in range(len(word)):
            b=set()
            for j in range(i,len(word)):
                if word[j] not in a:
                    break
                b.add(word[j])
                if b==a:
                    count+=1
        return count

        
        