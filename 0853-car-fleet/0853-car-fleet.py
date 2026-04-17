class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        carfleet=0
        size=len(speed)
        timetomeet=[0]*size
        joined=[]
        for i in range(size):
            joined.append([position[i],speed[i]])
        joined.sort()
        for i in range(size):
            timetomeet[i]=(target-joined[i][0])/joined[i][1]
        timetomeet.reverse()
        last_time=0
        for time in timetomeet:
            if time>last_time:
                carfleet+=1
                last_time=time
        return carfleet
        
        
       
        