class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        carfleet=0
        size=len(speed)
        timetomeet=[0]*size
        joined=[]
        for i in range(size):
            joined.append([position[i],speed[i]])
        joined.sort(reverse=True)
        for i in range(size-1,-1,-1):
            timetomeet[i]=(target-joined[i][0])/joined[i][1]
        
        last_time=0
        for time in timetomeet:
            if time>last_time:
                carfleet+=1
                last_time=time
        return carfleet
        
        
       
        