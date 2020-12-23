input = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

input = """1
2
3
5
6"""

from utils import Digraph # work on this class, use it for this purpose and others

g = Digraph(10)
print(g)


def count_paths(graph, visited, start, end):
	return 0


data = sorted(map(int, (line for line in input.split())))
# data.reverse()
print(data)

# graph = [[] for n in range(max(data) + 1)]
# graph[0] = [1,2,3]
# for n in data:
# 	neighbors = []
# 	for i in [1,2,3]:
# 		if (n + i) in data:
# 			neighbors.append(n+i)
# 	graph[n] = neighbors

# print(graph)

path = []
pathCount = 0
end = max(data)
visited = [False for n in range(end+1)]