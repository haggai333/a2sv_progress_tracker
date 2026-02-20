class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        ans = []

        for r in range(rows):
            new_row = []
            for c in range(cols):
                row_start = max(0, r - 1)
                row_end   = min(rows - 1, r + 1)
                col_start = max(0, c - 1)
                col_end   = min(cols - 1, c + 1)
                total = 0
                count = 0
                for i in range(row_start, row_end + 1):
                    for j in range(col_start, col_end + 1):
                        total += img[i][j]
                        count += 1

                new_row.append(total // count)

            ans.append(new_row)

        return ans
