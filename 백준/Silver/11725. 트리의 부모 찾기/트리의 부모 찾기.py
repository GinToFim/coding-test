import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)] # 트리 리스트 초기화
visited = [False] * (n + 1) # 방문 여부 테이블 초기화
parent = [0] * (n + 1) # 부모 테이블 초기화

for _ in range(n - 1) :
	a, b = map(int, input().split())
	tree[a].append(b)
	tree[b].append(a)

def dfs(tree, v, visited) :
	visited[v] = True

	for i in tree[v] :
		if not visited[i] :
			parent[i] = v
			dfs(tree, i, visited)

dfs(tree, 1, visited)

for i in range(2, n + 1) :
	print(parent[i])