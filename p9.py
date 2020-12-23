input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def pairsums(window):
	output = []
	for i in range(len(window)):
		for j in range(1,len(window)):
			output.append(window[i] + window[j])
	return output

windowsize = 25
data = []

with open("input/p9") as f:
	input = f.read()

for line in input.split():
	data.append(int(line))

for i in range(len(data) - windowsize):
	window = data[i:i+windowsize]
	check = data[i+windowsize]
	sums = pairsums(window)
	if check not in sums:
		print(check)
		break

invalidNum = check
for i in range(len(data)):
	for j in range(i+1,len(data)):
		test = data[i:j+1]
		if sum(test) == invalidNum:
			print(min(test) + max(test))
			break
