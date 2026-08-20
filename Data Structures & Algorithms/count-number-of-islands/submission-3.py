class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        traversed: Set[Tuple[int, int]] = set()
        res = 0
        def getValidNeighbors(i: int, j: int) -> Iterable[int]:
            left, right, up, down = (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
            neighbors = [left, right, up, down]
            in_bound_neighbors = (p for p in neighbors if 
                                    (0 <= p[0] < len(grid)) and 
                                    (0 <= p[1] < len(grid[i])))
            nonzero_neighbors = ((i,j) for (i,j) in in_bound_neighbors if grid[i][j] != '0')
            unexplored_neighbors = [p for p in nonzero_neighbors if p not in traversed]

            for p in unexplored_neighbors:
                traversed.add(p)
            return unexplored_neighbors

        def bfs(i: int, j: int) -> None:
            nonlocal res
            if grid[i][j] != '1' or (i, j) in traversed:
                return
            res += 1
            traversed.add((i, j))
            queue = [(i, j)]
            while queue:
                new_queue = []
                for plot in queue:
                    land_neighbors = getValidNeighbors(plot[0], plot[1])
                    new_queue.extend(land_neighbors)
                queue = new_queue

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                bfs(i, j)
        return res
            



