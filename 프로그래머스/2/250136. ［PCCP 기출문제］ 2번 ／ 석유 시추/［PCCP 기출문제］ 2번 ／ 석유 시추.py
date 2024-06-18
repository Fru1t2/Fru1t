from collections import deque

def bfs(land, visited, i, j):
    rows = len(land)
    cols = len(land[0])
    
    # 방향 벡터: 하, 좌, 우
    directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    
    queue = deque([(i, j)])
    size = 0
    min_col = j
    max_col = j
    
    while queue:
        x, y = queue.popleft()
        
        if not (0 <= x < rows and 0 <= y < cols):
            continue
        
        if visited[x][y] or land[x][y] == 0:
            continue
        
        visited[x][y] = True
        size += 1
        min_col = min(min_col, y)
        max_col = max(max_col, y)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            queue.append((nx, ny))
    
    return size, min_col, max_col

def solution(land):
    rows = len(land)
    cols = len(land[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = [0] * cols
    
    for j in range(cols):
        for i in range(rows):
            if land[i][j] == 1 and not visited[i][j]:
                size, min_col, max_col = bfs(land, visited, i, j)
                for k in range(min_col, max_col + 1):
                    result[k] += size
    
    return max(result)