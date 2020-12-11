def get_seat_id(input):
	id = 0
	for c in input:
		if c == "B" or c == "R":
			id = 2*id + 1
		else:
			id = 2*id
	return id

highestId = 0
idList = [0 for i in range(1024)]
with open("input/p5") as f:
	for line in f.read().splitlines():
		id = get_seat_id(line)
		if id > highestId:
			highestId = id
		idList[id] = 1
	for k,v in enumerate(idList):
		if v == 0:
			print(k)
print(highestId)
