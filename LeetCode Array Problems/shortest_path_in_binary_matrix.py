# Given an n x n binary matrix grid, return the
# length of the shortest clear path in the matrix.
# If there is no clear path, return -1.
#
# A clear path in a binary matrix is a path
# from the top-left cell (i.e., (0, 0)) to the bottom-right cell
# (i.e., (n - 1, n - 1)) such that:
#
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally
# connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        # check if source and target are not clear cells
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        N = len(grid)
        # offsets required for all 8 directions
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        q = deque()
        q.append((0, 0))  # starting point
        visited = {(0, 0)}

        # finds unvisited clear cells using 8 offsets
        def get_neighbours(x, y):
            for x_offset, y_offset in offsets:
                new_row = x + x_offset
                new_col = y + y_offset

                if 0 <= new_row < N and 0 <= new_col < N and not grid[new_row][new_col] and (
                        new_row, new_col) not in visited:
                    yield (new_row, new_col)

        current_distance = 1  # start with one clear cell
        # standard iterative BFS traversal
        while q:
            length = len(q)

            # loop through all the cells at the same distance
            for _ in range(length):
                row, col = q.popleft()

                if row == N - 1 and col == N - 1:  # reached target
                    return current_distance

                # loop though all valid neignbours
                for p in get_neighbours(row, col):
                    visited.add(p)
                    q.append(p)

            current_distance += 1  # update the level or distance from source

        return -1
