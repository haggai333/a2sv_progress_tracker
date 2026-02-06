class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1="qwertyuiop"
        line2="asdfghjkl"
        line3="zxcvbnm"
        dicvalue={}
        answer=[]
        for i in line1:
            dicvalue[i]=1
        for i in line2:
            dicvalue[i]=2
        for i in line3:
            dicvalue[i]=3
        for i in words:
            temp=""
            val=dicvalue[i[0].lower()]
            for  j in i:
                if val!=dicvalue[j.lower()]:
                    continue
                else:
                    temp+=j
            if len(temp)==len(i):
                answer.append(i)
        return answer

        
            
                
        
        