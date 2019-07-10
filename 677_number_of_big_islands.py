from collections import deque
class Solution:
    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """
    def numsofIsland(self, grid, k):
        if not grid:
            return 0
        row_num,col_num = len(grid),len(grid[0])
        visited,count = set(),0
        
        def get_neighbors(i,j):
            result = [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]
            if i == 0: result.remove((i-1,j))
            if i == row_num-1: result.remove((i+1,j))
            if j == 0: result.remove((i,j-1))
            if j == col_num-1: result.remove((i,j+1))
            return result
            
        for i in range(row_num):#traverse lines
            for j in range(col_num):#for each line, traverse each node
                if (i,j) in visited or grid[i][j] == 0 :
                    continue
                visited.add((i,j))#if first time visit
                size = 0
                queue=deque()
                queue.append((i,j))
                while len(queue):
                    (a,b)=queue.popleft()
                    size += 1
                    for neighbor in get_neighbors(a,b):
                        if (grid[neighbor[0]][neighbor[1]] == 1 
                        and neighbor not in visited):
                            visited.add(neighbor)
                            queue.append(neighbor)
                if size >= k:
                    count += 1
        return count