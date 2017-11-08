from getch import getch
tape = [0] * 5000
index = 0
tape[index] += 1
tape[index] += 1
index += 1
tape[index] += 1
tape[index] += 1
tape[index] += 1
tape[index] += 1
tape[index] += 1
while(tape[index] != 0):
	index -= 1
	tape[index] += 1
	index += 1
	tape[index] -= 1
	pass
tape[index] += 1
tape[index] += 1
tape[index] += 1
tape[index] += 1
tape[index] += 1
tape[index] += 1
tape[index] += 1
tape[index] += 1
while(tape[index] != 0):
	index -= 1
	tape[index] += 1
	tape[index] += 1
	tape[index] += 1
	tape[index] += 1
	tape[index] += 1
	tape[index] += 1
	index += 1
	tape[index] -= 1
	pass
index -= 1
print(chr(tape[index]), end="")
