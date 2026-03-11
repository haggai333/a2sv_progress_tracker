class Solution(object):
    def countVowelSubstrings(self, word):
        a=set("aeiou")
        count=0
        for i in range(len(word)):
            b=set()
            for j in range(i,len(word)):
                if word[j] in a:
                    b.add(word[j])
                else:
                    break
                if b==a:
                    count+=1
        return count

        
        