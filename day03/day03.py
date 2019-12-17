# Part 1
# Answer: 2427
wire_starting_position = [0, 0]
# Not quite sure why I have to explicitly convert this variable into a list for this to work but I do.
wire_01_path_positions = [list(wire_starting_position)]
wire_02_path_positions = [list(wire_starting_position)]

def calculate_wire_path_positions(wire_starting_position, wire_path):
	"""
	Returns a list of all the possible positions on a wire path based on initial point data.
	:param wire_starting_position list[list[int]]: A multi-dimensional list with an initial value [x, y] representing integers, indicating the central/starting point of the wire.
	:param wire_path list[str]: The path the wire travels. Example: "R8","U5","L5","D3" with R -> Right, U -> Up, L -> Left and D -> Down.
	"""
	all_wire_path_points = []
	current_wire_position = wire_starting_position[0]
	for path in wire_path:
		# This ensures that we include every number after the (R, U, L and D) direction.
		path_destination = int(path[1:])
		while(path_destination) > 0:
			if path.startswith("R"):
				current_wire_position[0] += 1
			elif path.startswith("U"):
				current_wire_position[1] += 1
			elif path.startswith("L"):
				current_wire_position[0] -= 1
			elif path.startswith("D"):
				current_wire_position[1] -= 1
			# Not quite sure why I have to explicitly convert this variable into a list for this to work but I do 
			# or else the last value of the 'list' gets appended 'n' number of times, which is definitely NOT what we want.
			all_wire_path_points.append(list(current_wire_position))
			path_destination -= 1
	return all_wire_path_points

def calculate_manhattan_distance(source, target):
	"""
	Formula for calculating the Manhattan Distance of two points.
	The Manhattan Distance, also known as taxicab geometry, is a form of geometry in which the usual distance function or metric of Euclidean geometry 
	is replaced by a new metric in which the distance between two points is the sum of the absolute differences of their Cartesian coordinates.
	Example: |x1 – x2| + |y1 – y2|.
	"""
	return abs(source[0] - target[0]) + abs(source[1] - target[1])

with open("input.txt") as f_handle:
	f_content = f_handle.readlines()
	wire_01_path, wire_02_path = [wire.strip().split(",") for wire in f_content]

	# :TEST DATA:
	# wire_01_path = ["R8", "U5", "L5", "D3"]
	# wire_02_path = ["U7", "R6", "D4", "L4"]
	# Using this setup the answer should be 6.
	# wire_01_path = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
	# wire_02_path = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
	# Using this setup the answer should be 159.
	# wire_01_path = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
	# wire_02_path = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
	# Using this setup the answer should be 135.

	wire_01_path_positions = calculate_wire_path_positions(wire_01_path_positions, wire_01_path)
	wire_02_path_positions = calculate_wire_path_positions(wire_02_path_positions, wire_02_path)
	# Removing duplicate positions. That is we don't want to include situations in which the wire has crossed itself.
	# We also must convert to tuple, in order to convert to set, in order to do an intersection set theory operation.
	wire_01_path_positions_no_dupes = set(wire_01_path_positions_no_dupe for wire_01_path_positions_no_dupe in set(tuple(wire_01_path_position) for wire_01_path_position in wire_01_path_positions))
	wire_02_path_positions_no_dupes = set(wire_02_path_positions_no_dupe for wire_02_path_positions_no_dupe in set(tuple(wire_02_path_position) for wire_02_path_position in wire_02_path_positions))
	wire_interect_points = tuple(wire_interect_point for wire_interect_point in (wire_01_path_positions_no_dupes).intersection(wire_02_path_positions_no_dupes))
	manhattan_distances = tuple(calculate_manhattan_distance(wire_starting_position, wire_interect_point) for wire_interect_point in wire_interect_points)
	print(min(manhattan_distances))