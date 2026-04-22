class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def shipable(size):
            day = 1
            counts = 0

            for w in weights:
                if counts+ w > size:
                    day += 1
                    counts = 0
                counts += w

            return day <= days

        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = (l + r) // 2

            if shipable(mid):
                r = mid
            else:
                l = mid + 1

        return l
