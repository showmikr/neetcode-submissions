from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            adj_list[c].append(p)
        finished = set()
        
        traversing = set()
        res = True
        def dfs(course):
            if course in finished:
                return
            if course in traversing:
                nonlocal res
                res = False
                return
            traversing.add(course)
            for p in adj_list[course]:
                dfs(p)
            traversing.remove(course)
            finished.add(course)

        for c in adj_list:
            print(c)
            dfs(c)
        return res

        
