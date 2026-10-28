def dfs(u):
    visited[u] = True
    print(u,end=' ')
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)  
visited = [False]*(n+1)
dfs(1)