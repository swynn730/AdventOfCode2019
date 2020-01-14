# Part 1
# Answer: 212460
from itertools import permutations

class ParameterMode():
	POSITION = 0
	INTERMEDIATE = 1

class Amplifier():
	def __init__(self, code):
		self.code = code

def extract_intcode_program(integer_list, *args):
	instruction_pointer = 0
	output = 0
	integer_list_len = len(integer_list)
	while(instruction_pointer < integer_list_len):
		# Extracting the invidual numbers that make up the instruction code.
		instruction_code = [x for x in str(integer_list[instruction_pointer])]

		# Preserving negative numbers.
		for idx, num in enumerate(instruction_code):
		    if num == "-":
		        instruction_code[idx + 1] = "-" + instruction_code[idx + 1]

		# Cleaning up undesirable symbols.
		while "-" in instruction_code:
		    instruction_code.remove("-")

		# Padding each number so that it has a consistent instruction code length and maps to ABCDE.
		while(len(instruction_code) < 5):
			instruction_code.insert(0, "0")

		opcode = "".join(instruction_code[-2::])

		parameter_modes = []

		# Keeping track of which mode each instruction parameter needs to be in.
		for instruction_code_num in instruction_code[:-2]:
			if int(instruction_code_num) == ParameterMode.POSITION:
				parameter_modes.insert(0, True)
			else:
				parameter_modes.insert(0, False)

		if opcode == "01":
			# Add first and second parameter and store in third. Skip 4 spaces ahead when done.
			param_00 = integer_list[instruction_pointer + 1]
			param_01 = integer_list[instruction_pointer + 2]
			param_02 = integer_list[instruction_pointer + 3]
			# Determine the mode.
			mode_00 = integer_list[param_00] if parameter_modes[0] else param_00
			mode_01 = integer_list[param_01] if parameter_modes[1] else param_01
			integer_list[param_02] = mode_00 + mode_01
			instruction_pointer += 4

		elif opcode == "02":
			# Multiply first and second parameter and store in third. Skip 4 spaces ahead when done.
			param_00 = integer_list[instruction_pointer + 1]
			param_01 = integer_list[instruction_pointer + 2]
			param_02 = integer_list[instruction_pointer + 3]
			# Determine the mode.
			mode_00 = integer_list[param_00] if parameter_modes[0] else param_00
			mode_01 = integer_list[param_01] if parameter_modes[1] else param_01
			integer_list[param_02] = mode_00 * mode_01
			instruction_pointer += 4

		elif opcode == "03":
			# Set first parameter equal to the user supplied value. Skip 2 spaces ahead when done.
			param_00 = integer_list[instruction_pointer + 1]
			# Don't need to determine the mode here since the mode by default will always be POSITION.
			# I had trouble understanding the instructions for this problem so the idea for the following two lines of code came from here:
			# https://github.com/aitc-h/advent2019/blob/master/7/7part1.py
			# Sets this to whatever the phase setting currently is. The phase setting is considered the first or initial input.
			integer_list[param_00] = args[0]
			# The second input value now becomes the first or initial input and this new value is now used until the code is finished being processed.
			args = args[1:]
			instruction_pointer += 2

		elif opcode == "04":
			# Output the value of the only parameter. Skip 2 spaces ahead when done.
			param_00 = integer_list[instruction_pointer + 1]
			# Determine the mode.
			mode_00 = integer_list[param_00] if parameter_modes[0] else param_00
			#print(mode_00)
			output = mode_00
			instruction_pointer += 2

		elif opcode == "05":
			# If the first parameter is non-zero, set the instruction pointer to the value of the second parameter, otherwise do "nothing"/skip 3 spaces ahead when done. 
			# But if the instruction modifies the instruction pointer there's no need to skip spaces automatically.
			param_00 = integer_list[instruction_pointer + 1]
			param_01 = integer_list[instruction_pointer + 2]
			# Determine the mode.
			mode_00 = integer_list[param_00] if parameter_modes[0] else param_00
			mode_01 = integer_list[param_01] if parameter_modes[1] else param_01
			instruction_pointer = mode_01 if mode_00 != 0 else (instruction_pointer + 3)

		elif opcode == "06":
			# If the first parameter is zero, set the instruction pointer to the value of the second parameter, otherwise do "nothing"/skip 3 spaces ahead when done. 
			# But if the instruction modifies the instruction pointer there's no need to skip spaces automatically.
			param_00 = integer_list[instruction_pointer + 1]
			param_01 = integer_list[instruction_pointer + 2]
			# Determine the mode.
			mode_00 = integer_list[param_00] if parameter_modes[0] else param_00
			mode_01 = integer_list[param_01] if parameter_modes[1] else param_01
			instruction_pointer = mode_01 if mode_00 == 0 else (instruction_pointer + 3)

		elif opcode == "07":
			# If the first parameter is less than the second parameter, store 1 in the position given by the third parameter, otherwise store 0. Skip 4 spaces ahead when done.
			param_00 = integer_list[instruction_pointer + 1]
			param_01 = integer_list[instruction_pointer + 2]
			param_02 = integer_list[instruction_pointer + 3]
			# Determine the mode.
			mode_00 = integer_list[param_00] if parameter_modes[0] else param_00
			mode_01 = integer_list[param_01] if parameter_modes[1] else param_01
			integer_list[param_02] = 1 if mode_00 < mode_01 else 0
			instruction_pointer += 4

		elif opcode == "08":
			# If the first parameter is equal to the second parameter, store 1 in the position given by the third parameter, otherwise store 0. Skip 4 spaces ahead when done.
			param_00 = integer_list[instruction_pointer + 1]
			param_01 = integer_list[instruction_pointer + 2]
			param_02 = integer_list[instruction_pointer + 3]
			# Determine the mode.
			mode_00 = integer_list[param_00] if parameter_modes[0] else param_00
			mode_01 = integer_list[param_01] if parameter_modes[1] else param_01
			integer_list[param_02] = 1 if mode_00 == mode_01 else 0
			instruction_pointer += 4

		elif opcode == "99":
			break

		else:
			# Unknown opcode.
			instruction_pointer += 1

	return output

with open("input.txt") as f_handle:
	f_content = f_handle.read()
	code = [int(num) for num in f_content.strip().split(",")]

number_of_amplifiers = 5
max_thruster_signal = 0
thruster_signals = []
# Creates permutations of a list "x" elements long with each element going from 0 -> "x".
for phase_setting in permutations(range(number_of_amplifiers)):
	starting_input = 0
	# Each permutation is tested against "x" number of amplifiers.
	for num in range(number_of_amplifiers):
		amplifier = Amplifier(code)
		starting_input = extract_intcode_program(amplifier.code, phase_setting[num], starting_input)
	# Store the result of each permutation (phase sequence) as it has been processed by "x" number of amplifiers.
	thruster_signals.append(starting_input)

max_thruster_signal = max(thruster_signals)
print(max_thruster_signal)