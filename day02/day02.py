# Part 1
# Answer: 4090689 
def calculate_opcode_01(pos00, pos01):
	return pos00 + pos01

def calculate_opcode_02(pos00, pos01):
	return pos00 * pos01

def extract_intcode_program(integer_list):
	start_pos = 0

	for idx, num in enumerate(integer_list):
		# Ensures we move forward 4 positions after processing each opcode.
		if not (idx % 4 == 0):
			continue
		if num == 1:
			add_pos_00 = integer_list[idx + 1]
			add_pos_01 = integer_list[idx + 2]
			sum_pos = integer_list[idx + 3]
			opcode_01_sum = calculate_opcode_01(integer_list[add_pos_00], integer_list[add_pos_01])
			integer_list[sum_pos] = opcode_01_sum
			start_pos += 4
		elif num == 2:
			multiply_pos_00 = integer_list[idx + 1]
			multiply_pos_01 = integer_list[idx + 2]
			product_pos = integer_list[idx + 3]
			opcode_02_product = calculate_opcode_02(integer_list[multiply_pos_00], integer_list[multiply_pos_01])
			integer_list[product_pos] = opcode_02_product
			start_pos += 4
		elif num == 99:
			break
		else:
			# Unknown opcode.
			continue

	return integer_list

with open("input.txt") as f_handle:
	f_content = f_handle.read()
	integer_list = [int(num) for num in f_content.strip().split(",")]
	# Setting the program to the "1202 program alarm state".
	# :NOTE: If using the test data, comment the following two lines out.
	integer_list[1] = 12
	integer_list[2] = 2
	# :TEST DATA:
	# integer_list = [1, 0, 0, 0, 99]				#-> 2, 0, 0, 0, 99
	# integer_list = [2, 3, 0, 3, 99]				#-> 2, 3, 0, 6, 99
	# integer_list = [2, 4, 4, 5, 99, 0]			#-> 2, 4, 4, 5, 99, 9801
	# integer_list = [1, 1, 1, 4, 99, 5, 6, 0, 99]	#-> 30, 1, 1, 4, 2, 5, 6, 0, 99
	print(extract_intcode_program(integer_list)[0])

# Part 2
# Answer: 7733
target_output = 19690720
noun = range(0, 100)
verb = range(0, 100)
input_noun = None
input_verb = None
integer_list = []

with open("input.txt") as f_handle:
	f_content = f_handle.read()
	integer_list = [int(num) for num in f_content.strip().split(",")]

final_output = 0
# Brute force for the win! But at least we can bail out of the nested loop as soon as we get the correct output.
for n in noun:
	for v in verb:
		# Resetting the 'memory' of the program.
		integer_list_copy = integer_list[:]
		integer_list_copy[1] = n
		integer_list_copy[2] = v
		final_output = extract_intcode_program(integer_list_copy)[0]
		if final_output == target_output:
			input_noun = n
			input_verb = v
			break
	else:
		continue	# Only execute if the inner loop did NOT break.
	break	# Only execute if the inner loop DID break.

print(100 * input_noun + input_verb)