class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        listofval=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        listans={}
        for i in words:
            answer=""
            for j in i:
                answer+=listofval[ord(j.lower())-ord('a')]
            if answer not in listans:
                listans[answer]=1
        return len(listans)

        