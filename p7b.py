class Bag:
	count = 0
	color = ''
	children = []
	parent = None

	def __init__(self, count, color):
		self.count = count
		self.color = color
		self.children = []
		self.parent = None

	def __str__(self):
		return str(self.count) + " " + self.color + " => [" + ','.join(map(str,self.children)) + "]"
		# return str(self.count) + " " + self.color

	def addChild(self, child):
		child.parent = self
		self.children.append(child)

	def numChildrenInBag(self):
		return sum(c.count for c in self.children)

	def bagsWithin(self):
		if not self.children:
			return 0
		else:
			t = self.count * (self.numChildrenInBag() + sum(b.bagsWithin() for b in self.children))
			print(t)
			return t # self.count * self.numChildrenInBag() + sum(b.bagsWithin() for b in self.children)

input = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

with open("input/p7") as f:
	input = f.read()

root = Bag(1, "shiny gold")
info = {}

# read info into a dict for easy access
for line in input.splitlines():
	words = line.split()
	outer = ' '.join(words[0:2])
	if words[4] == "no":
		info[outer] = None
	else:
		inner = words[4:]
		contained = []
		while len(inner) > 0:
			contained.append({"count": int(inner[0]), "color": ' '.join(inner[1:3])})
			inner = inner[4:]
		info[outer] = contained

#starting at the root:
#find current node's children, create Bag objects
flag = False
childStack = []
curr = root
while not flag:
	if info[curr.color]:
		for ch in info[curr.color]:
			b = Bag(ch["count"], ch["color"])
			curr.addChild(b)
			childStack.append(b)
	if not childStack:
		flag = True
	else:
		curr = childStack.pop(0)

print(root)
print(root.bagsWithin())
