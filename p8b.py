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

# program is list of instructions as normal
# index is the index to try changing (either from nop to jmp or vice versa)
# returns a tuple (val,terminated)
# acc: value of the accumulator
# terminated: whether the program looped (False) or properly exited (True)
def run_program(program, index):
	visited = [0 for i in range(len(program))]
	pc = 0
	flag = False
	acc = 0
	terminated = False
	while not flag:
		if pc >= len(program):
			terminated = True
			flag = True
		elif visited[pc] == 1:
			flag = True
		else:
			visited[pc] = 1
			curr = program[pc].split()
			inst = curr[0]
			val = int(curr[1])
			if inst == "nop" or (pc == index and inst == "jmp"):
				pc += 1
			elif inst == "acc":
				acc += val
				pc += 1
			elif inst == "jmp" or (pc == index and inst == "nop"):
				pc += val
			else:
				print("unhandled instruction")
				flag = True
	return (acc, terminated)


program = input.splitlines()
nopOrJmp = []
for index, inst in enumerate(program):
	if inst[0:3] == "nop" or inst[0:3] == "jmp":
		nopOrJmp.append(index)

print(nopOrJmp)
for index in nopOrJmp:
	val,terminated = run_program(program,index)
	if terminated:
		print(val)