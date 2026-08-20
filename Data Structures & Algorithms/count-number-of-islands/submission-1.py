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
            return [p for p in in_bound_neighbors if p not in traversed and grid[p[0]][p[1]] != '0']

        def bfs(i: int, j: int) -> None:
            nonlocal res
            if grid[i][j] != '1' or (i, j) in traversed:
                return
            queue = [(i, j)]
            while queue:
                new_queue = []
                for plot in queue:
                    traversed.add(plot)
                    land_neighbors = [n for n in getValidNeighbors(plot[0], plot[1])]
                    traversed.update(land_neighbors)
                    new_queue.extend(land_neighbors)
                queue = new_queue
            res += 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                bfs(i, j)
        return res
            



