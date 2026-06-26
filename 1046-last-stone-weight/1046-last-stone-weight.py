class Solution(object):
    def lastStoneWeight(self, stones):
        heap=[]
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap)>1:
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)
            if x==y:
                continue
            elif x>y:
                heapq.heappush(heap,-(x-y))
            else:
                heapq.heappush(heap,-(y-x))
        if not heap:
            return 0
        return -heap[0]

        