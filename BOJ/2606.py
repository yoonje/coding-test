from collections import deque

node_num = int(input())
edge_num = int(input())

adj = [[] for _ in range(node_num + 1)]
visited = [False] * (node_num + 1)

for _ in range(edge_num):
    x, y = map(int, input().split(" "))
    adj[x].append(y)
    adj[y].append(x)


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not (visited[v]):
            visited[v] = True
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)
    return visited


count = 0
for item in bfs(1):
    if item is True:
        count += 1

print(count - 1)
