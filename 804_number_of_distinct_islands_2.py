from collections import deque
class Solution:
    """
    @param grid: the 2D grid
    @return: the number of distinct islands
    """
    def numDistinctIslands2(self, grid):

        row_num,col_num = len(grid),len(grid[0])
        visited,island = set(),set()
        
        for i in range(row_num):#traverse lines
            for j in range(col_num):#for each line, traverse each node
                if (i,j) in visited or grid[i][j] == 0 :
                    continue
                visited.add((i,j))#if first time visit
                path = set()
                queue=deque()
                queue.append((i,j))
                while queue:#BFS
                    cur=queue.popleft()
                    path.add(complex(cur[0],cur[1]))
                    for neighbor in Solution.get_neighbors(cur[0],cur[1],row_num,col_num):#append its neighbor
                        if (grid[neighbor[0]][neighbor[1]] == 1 and 
                        neighbor not in visited):
                            visited.add(neighbor)
                            queue.append(neighbor)
                if path:
                    island.add(Solution.canonical(path))
        return len(island)
        
    @staticmethod  
    def get_neighbors(i,j,row_num,col_num):
        result = [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]
        if i == 0: result.remove((i-1,j))
        if i == row_num-1: result.remove((i+1,j))
        if j == 0: result.remove((i,j-1))
        if j == col_num-1: result.remove((i,j+1))
        return result
        
    @staticmethod
    def canonical(shape):
        def translate(shape):
            w = complex(min(z.real for z in shape),
                        min(z.imag for z in shape))
            return sorted(str(z-w) for z in shape)

        ans = None
        for k in range(4):
            ans = max(ans, translate([z * (1j)**k for z in shape]))
            ans = max(ans,  translate([complex(z.imag, z.real) * (1j)**k
                                       for z in shape]))
        return tuple(ans)