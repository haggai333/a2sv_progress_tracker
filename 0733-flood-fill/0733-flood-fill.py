class Solution(object):
    def floodFill(self, image, sr, sc, color):
        visited=set()
        og=image[sr][sc]
        def dfs(i,j):
            if i<0 or i>len(image)-1 or j<0 or j>len(image[0])-1 or (i,j) in visited or image[i][j]!=og:
                return
            visited.add((i,j))
            image[i][j]=color
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        dfs(sr,sc)
        return image

        