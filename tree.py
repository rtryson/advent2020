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
		return str(self.count) + " " + self.color

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
			#print(t)
			return t # self.count * self.numChildrenInBag() + sum(b.bagsWithin() for b in self.children)


root = Bag(1, "shiny gold")
a = Bag(5, "pale green")
b = Bag(5, "faded gold")
c = Bag(3, "dark plum")
d = Bag(5, "clear teal")
e = Bag(5, "s white")
f = Bag(1, "m coral")
g = Bag(5, "g")
h = Bag(2, "h")
i = Bag(2, "i")
j = Bag(1, "j")
a.addChild(c)
a.addChild(d)
a.addChild(e)
a.addChild(f)
b.addChild(g)
b.addChild(h)
b.addChild(i)
b.addChild(j)
root.addChild(a)
root.addChild(b)

print(a)
print(e.parent)
print(root.bagsWithin())
