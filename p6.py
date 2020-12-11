total = 0
with open("input/p6") as f:
	group = ''
	for line in f.read().splitlines():
		if line:
			group += line
		else:
			total += len(''.join(set(group)))
			group = ''
print(total)

altTotal = 0
with open("input/p6") as f:
	counts = [0 for i in range(26)]
	numInGrp = 0
	for line in f.read().splitlines():
		if line:
			numInGrp += 1
			for c in line:
				counts[ord(c)-ord('a')] += 1
		else:
			for l in counts:
				if l == numInGrp:
					altTotal += 1
			numInGrp = 0
			counts = [0 for i in range(26)]
print(altTotal)