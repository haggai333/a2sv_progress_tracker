class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        l=0
        r=0
        answer=0
        while l<len(players) and r<len(trainers):
            if players[l]<=trainers[r]:
                answer+=1
                l+=1
                r+=1
            else:
                l+=1
        return answer

        