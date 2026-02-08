class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        valuelist=[]
        answer=[]
        for i in words:
            temp={}
            for j in i:
                if j in temp:
                    temp[j]+=1
                else:
                    temp[j]=1
            valuelist.append(temp)
        for i in words[0]:
            mini=376655
            for j in valuelist:
                if i in j:
                    mini=min(j[i],mini)
                else:
                    mini=0
                    break
            if i not in answer:            
                for k in range(mini):
                     answer.append(i)
        return answer


            


            

        