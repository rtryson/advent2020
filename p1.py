
target = 2020
with open('input/p1') as f:
	input = [int(c) for c in f.read().splitlines()]
	for i in range(len(input)):
		for j in range(i+1,len(input)):
			if input[i] + input[j] == target:
				print(input[i]*input[j])