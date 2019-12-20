import copy
# Part 1
# Answer: 245089
# Needed some help with part 1, because even though the original algorithm I came up with worked on the test data it didn't work with the real data.
# I kept getting memory and recursion errors. :(
# Looking at the following solution gave me the last 5% I needed to get my code correct though: 
# https://github.com/xADDBx/Advent-of-Code/blob/master/2019/Day%206/Day6_1.py
# THANK YOU ANONYMOUS PERSON!
orbit_map = {}
with open("input.txt") as f_handle:
	f_content = f_handle.readlines()
	# :TEST DATA FOR PART 1:
	# f_content = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
	# The answer for the total number of direct and indirect orbits is 42.
	# :TEST DATA FOR PART 2:
	# f_content = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"]
	# The answer for the minimum number of orbital transfers is 4.
	for orbit in f_content:
		# The parent is the object being orbited.
		# The child is the object orbiting the parent.
		parent, child = orbit.strip().split(")")
		# Here's a trick. Make the child the "focus" in our dictionary rather than the parent. 
		# This will make getting the orbital route much easier.
		orbit_map[child] = orbit_map.get(child, []) + [parent]

# Create a copy because we want to read the data from one while updating the other. This algorithm won't work without it.
orbit_map_copy = copy.deepcopy(orbit_map)
orbit_map_keys = orbit_map.keys()
for orbit_map_key in orbit_map_keys:
	orbit_map_values = orbit_map[orbit_map_key]
	def traverse(op, val):
		"""
		Utility function for getting an orbit's orbital route.
		:param dict op: This holds all of the orbital data with the orbiting object being a child and the object being orbited the parent.
		:param str val: This contains the object being orbited (the parent object). 
		"""
		# The only key that won't be in our obit map is "COM".
		if val not in op:
			return [val]
		else:
		# Basically we keep checking for a parent until we reach "COM".
		# Example: (Starting with F, see the test data above)
		# F -> E -> D -> C -> B -> COM
		# We have to do [0] because the new val data will be in a list but there will only ever be 1 element for the val in the original orbit map.
			return traverse(op, op[val][0]) + [val]
	# Clear out existing content and update the copy with the complete orbit route. This way we don't get a duplicate entry at the very beginning of the list.
	orbit_map_copy[orbit_map_key] = []
	for orbit_map_value in orbit_map_values:
		orbit_map_copy[orbit_map_key] += traverse(orbit_map, orbit_map_value)

# Now that we've got the route for each child object (orbiting object), add the total amount of traversals towards "COM" up.
total_direct_and_indirect_orbits = 0
orbit_map_copy_values = orbit_map_copy.values()
for orbit_map_copy_value in orbit_map_copy_values:
	total_direct_and_indirect_orbits += len(orbit_map_copy_value)

print(total_direct_and_indirect_orbits)

# Part 2
# Answer: 511
# :THIS CODE IS FOR PART 2 ONLY:
san_orbits = orbit_map_copy["SAN"]
you_orbits = orbit_map_copy["YOU"]
# Substract the common objects from each route to get the unique objects. 
# The summation or in this case union of the unique objects together represents the minimum number of orbital transfers
# required to move from the object YOU are orbiting to the object SAN is orbiting.
# (Between the objects they are orbiting NOT between YOU and SAN).
intersecting_orbits = set(san_orbits).intersection(set(you_orbits))
print(len(set(san_orbits).difference(intersecting_orbits).union(set(you_orbits).difference(intersecting_orbits))))