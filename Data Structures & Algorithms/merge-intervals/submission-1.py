class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            i_start, i_end = intervals[i]
            to_merge = [i_start, i_end]
            j = i + 1
            while j < len(intervals):
                j_start, j_end = intervals[j]
                m_start, m_end = to_merge
                if j_start > m_end:
                    break
                to_merge = [m_start, max(j_end, m_end)]
                j += 1
            res.append(to_merge)
            i = j

        return res
