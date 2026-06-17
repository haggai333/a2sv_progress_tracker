class Solution(object):
    def findCircleNum(self, isConnected):
        answer=0
        def dfs(city):
            for j in range(len(isConnected[city])):
                if isConnected[city][j]==1 and j not in self.visited:
                    self.visited.add(j)
                    dfs(j)
        self.visited=set()
        for city in range(len(isConnected)):
            if city not in self.visited:
                answer+=1
                self.visited.add(city)
                dfs(city)
        return answer
        