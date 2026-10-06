from collections import deque
from collections import defaultdict
def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [0] * (n+1)
    visited[0] = 1
    queue = deque([0])
    while queue:
        node = queue.popleft()
        vertex = 1
        edge = 0
        for neighbors in graph[node]:
            
    