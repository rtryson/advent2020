
target = 2020
with open('input/p1') as f:
	input = [int(c) for c in f.read().splitlines()]
	for i in range(len(input)):
		for j in range(i+1,len(input)):
			for k in range(j+1,len(input)):
				if input[i] + input[j] + input[k] == target:
					print(input[i]*input[j]*input[k])