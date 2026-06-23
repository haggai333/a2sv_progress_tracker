class Solution(object):
    def validPath(self, n, edges, source, destination):
        if source==destination:
            return True
        graph=[]
        self.answer=False
        for i in range(len(edges)):
                p,j=edges[i]
                while len(graph)<p+1 or len(graph)<j+1:
                    graph.append([])
                graph[p].append(j)
                graph[j].append(p)
        visited=set()
        def dfs(i):
            if self.answer:
                return
            if i <len(graph) and i>-1:
                for p in graph[i]:
                    if p not in visited:
                        visited.add(p)
                        dfs(p)
                    if p==destination:
                        self.answer=True
                        return
        dfs(source)
        return self.answer
                
        