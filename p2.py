def parse_line(line):
	words = line.split()
	limit = words[0].split('-')
	low = int(limit[0])
	high = int(limit[1])
	c = words[1][0]
	pw = words[2]
	return low,high,c,pw

def check_policy(low,high,c,pw):
	check = pw.count(c)
	return check >= low and check <= high

def check_policy_alt(low,high,c,pw):
	low_match = (pw[low-1] == c)
	high_match = (pw[high-1] == c)
	return low_match ^ high_match

numValid = 0
numValidAlt = 0
with open("input/p2") as f:
	for line in f.read().splitlines():
		if line:
			low, high, c, pw = parse_line(line)
			if check_policy(low,high,c,pw):
				print(low,high,c,pw)
				numValid += 1
			if check_policy_alt(low,high,c,pw):
				numValidAlt += 1
print(numValid, numValidAlt)