input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

with open("input/p7") as f:
	input = f.read()

searchColors = ["shiny gold"]
finalList = []
flag = False

while not flag:
	newSearchColors = []
	print("search: ", searchColors)
	startCount = len(finalList)
	for line in input.splitlines():
		words = line.split() 
		# 0&1 = color, 2&3 = garbage, 4 and beyond = containing colors (in groups of 4)
		outerColor = ' '.join(words[0:2])
		containing = words[4:]
		while len(containing) > 0:
			numOfColor = containing[0] #not used now but could be later
			testColor = ' '.join(containing[1:3])
			if testColor in searchColors and outerColor not in newSearchColors:
				newSearchColors.append(outerColor)
			containing = containing[4:]
	finalList = list(set(finalList + newSearchColors))
	print("final: ", finalList)
	searchColors = newSearchColors
	endCount = len(finalList)
	if startCount == endCount:
		flag = True

print(finalList, len(finalList))

