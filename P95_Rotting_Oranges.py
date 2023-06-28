# prob_link: https://www.codingninjas.com/studio/problems/rotting-oranges_8230701?challengeSlug=striver-sde-challenge&leftPanelTab=0

def minTimeToRot(grid, n, m):
    # Write your code here.
    rows = len(grid)
    cols = len(grid[0])
    vis = [[0 for j in range(cols)] for i in range(rows)]
    direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    from collections import deque
    dq = deque()
    totaloranges = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                vis[i][j] = 1
                dq.append((i, j))
            elif grid[i][j] == 1:
                totaloranges += 1

    if totaloranges == 0:
        return 0
    level = 0
    while (len(dq) > 0):
        level += 1
        sz = len(dq)
        for i in range(sz):
            r, c = dq.popleft()
            for x, y in direction:
                row = r + x
                col = c + y
                if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == 1 and vis[row][col] == 0:
                    vis[row][col] = 1
                    totaloranges -= 1
                    dq.append((row, col))
                    if totaloranges == 0:
                        return level

    return -1

