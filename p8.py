input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

with open("input/p8") as f:
	input = f.read()

program = input.splitlines()
pc = 0

visited = [0 for i in range(len(program))]
flag = False
acc = 0
while not flag:
	if visited[pc] == 1:
		flag = True
	else:
		visited[pc] = 1
		curr = program[pc].split()
		inst = curr[0]
		val = int(curr[1])
		if inst == "nop":
			pc += 1
		elif inst == "acc":
			acc += val
			pc += 1
		elif inst == "jmp":
			pc += val
		else:
			print("unhandled instruction")
			flag = True
print(acc)