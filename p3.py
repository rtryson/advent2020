# input = ["..##.......",
# "#...#...#..",
# ".#....#..#.",
# "..#.#...#.#",
# ".#...##..#.",
# "..#.##.....",
# ".#.#.#....#",
# ".#........#",
# "#.##...#...",
# "#...##....#",
# ".#..#...#.#"]

with open("input/p3") as f:
	input = f.read().splitlines()
	width = len(input[0])
	height = len(input)
	x_deltas = [1,3,5,7,1]
	y_deltas = [1,1,1,1,2]
	answer = 1
	for i in range(5):
		x = 0
		x_delta = x_deltas[i]
		y = 0
		y_delta = y_deltas[i]
		trees = 0

		while(y < height):
			# move
			x = (x + x_delta) % width
			y = (y + y_delta)
			if y < height and input[y][x] == "#":
				trees += 1
		print(trees)
		answer *= trees
	print(answer)