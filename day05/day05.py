# Part 1
# Answer: 4887191
# Had to "cheat" a bit here. The instructions for this puzzle were wordy and I had trouble understanding them.
# Therefore I needed some "inspiration" -> https://pastebin.com/0k9ZTur6
# I still like my code better though. :)
class ParameterMode():
	POSITION = 0
	INTERMEDIATE = 1

def extract_intcode_program(user_input_instruction, integer_list):
	instruction_pointer = 0
	integer_list_len = len(integer_list)
	while(instruction_pointer < integer_list_len):
		# Extracting the invidual numbers that make up the instruction code.
		instruction_code = [x for x in str(integer_list[instruction_pointer])]

		# Perserving negative numbers.
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
			# Set first parameter equal to the user supplied value. Don't need to determine the mode here since the mode by default will always be POSITION.
			param_00 = integer_list[instruction_pointer + 1]
			integer_list[param_00] = user_input_instruction
			instruction_pointer += 2
			#
		elif opcode == "04":
			# Output the value of the only parameter.
			param_00 = integer_list[instruction_pointer + 1]
			# Determine the mode.
			mode_00 = integer_list[param_00] if parameter_modes[0] else param_00
			print(mode_00)
			instruction_pointer += 2

		elif opcode == "99":
			break

		else:
			# Unknown opcode.
			instruction_pointer += 1

	return integer_list

with open("input.txt") as f_handle:
	f_content = f_handle.read()
	integer_list = [int(num) for num in f_content.strip().split(",")]
	user_input_instruction = 1
	extract_intcode_program(user_input_instruction, integer_list)

# Part 2
# Answer: