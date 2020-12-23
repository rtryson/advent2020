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

with open("input/p10") as f:
	input = f.read()

port = 0
d1 = 0
d3 = 0
for adapter in sorted(map(int, input.split())):
	if adapter - port == 1:
		d1 += 1
	if adapter - port == 3:
		d3 += 1
	port = adapter

d3 += 1 # for your device

print(d1, d3, d1*d3)