class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range (1, len(intervals)):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            last_start = res[-1][0]
            last_end = res[-1][1]
            if cur_start <= last_end:
                res[-1][1] = max(last_end, cur_end)
            else:
                res.append(intervals[i])
        return res
