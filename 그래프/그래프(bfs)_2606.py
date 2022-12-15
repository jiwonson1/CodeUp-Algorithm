# 연결된 컴퓨터 그래프를 만들고, 연결되어있으면 1, 아니면 0
# 1부터 시작 큐에 1 append
# visited도 변경해줌
# n+1을 하는 이유는 0은 없다고 생각하는 것?

#[그래프는 연결여부용, visited는 방문체크용]

from collections import deque

n = int(input())
m = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
visited = [0] * (n + 1)
q = deque()
q.append(1)
visited[1] = 1
cnt = 0

while q:
    now = q.popleft()
    for i in range(1, n + 1):
        if graph[now][i] == 1 and visited[i] == 0:  #연결되어 있고, 방문한적 없으면
            visited[i] = 1
            q.append(i)
            cnt += 1
print(cnt)
