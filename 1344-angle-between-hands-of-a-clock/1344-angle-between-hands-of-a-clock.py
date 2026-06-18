class Solution(object):
    def angleClock(self, hour, minutes):
        mino=float(minutes)/5
        houro=hour+float(minutes)/60
        dif=min(abs(houro-mino),abs(12.0-(houro-mino)))
        angle=(dif/12)*360
        return min(angle,360-angle)
        
        