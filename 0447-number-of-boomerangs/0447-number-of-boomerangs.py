class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0

        result = 0

        for center_x, center_y in points:
            distance_count = defaultdict(int)

            for x, y in points:
                dx = center_x - x
                dy = center_y - y
                distance = dx * dx + dy * dy

                result += 2 * distance_count[distance]
                distance_count[distance] += 1

        return result
                
        