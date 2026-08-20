class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        visiting = set() 
        def dfs(crs: int) -> bool:
            if crs in visiting:
                return False
            prereqs = adj_list[crs]
            if not prereqs:
                return True
            visiting.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            adj_list[crs] = []
            return True
        
        return all(dfs(c) for c in adj_list if adj_list[c])

            


                


