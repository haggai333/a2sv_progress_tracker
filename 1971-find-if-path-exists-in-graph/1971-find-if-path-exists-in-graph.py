class Solution(object):
    def validPath(self, n, edges, source, destination):
        if source==destination:
            return True
        graph=[[] for _ in range(n)]

        self.answer=False
        for i in range(len(edges)):
                p,j=edges[i]
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
                        if self.answer:
                            return
                    if p==destination:
                        self.answer=True
                        return
        dfs(source)
        return self.answer
                
        