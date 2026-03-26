class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        answer=0
        r=len(people)-1
        l=0
        while r>=l:
            if people[r]+people[l]<=limit:
                l+=1
            answer+=1
            r-=1
        return answer
        
            
                    
                    
                
            
                
                
        print(answer)


            
        