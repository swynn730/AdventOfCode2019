import math

# Part 1
# Answer: 3335787
module_fuel_requirements = []
total_fuel_requirement = 0
with open("input.txt") as f_handle:
	f_content = f_handle.readlines()
	for module_mass in f_content:
		module_fuel_requirements += [math.floor(int(module_mass.strip()) / 3) - 2]
	total_fuel_requirement = sum(module_fuel_requirements)

print(total_fuel_requirement)

# Part 2
# Answer: 5000812
def calculate_total_module_fuel_requirements(module_mass):
	"""
	When given a base mass, calculate the total fuel expenditure.
	:param module_mass: The mass of the module as fuel is used, used to calculate total fuel expenditure.
	"""
	if module_mass < 1:
		return 0
	return calculate_total_module_fuel_requirements(math.floor(module_mass / 3) - 2) + module_mass

module_fuel_requirements = []
total_fuel_requirement = 0
with open("input.txt") as f_handle:
	f_content = f_handle.readlines()
	for base_module_mass in f_content:
		base_module_mass = int(base_module_mass.strip())
		# Since we included the base mass of the module in our calculations we have to be sure to substract that out at the end.
		# Example: For a mass of 100756.
		# 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
		# Notice we're not suppose to include the 100756 but we do here so we need to subtract that out to get the correct answer.
		module_fuel_requirements += [calculate_total_module_fuel_requirements(base_module_mass) - base_module_mass]
	total_fuel_requirement = sum(module_fuel_requirements)

print(total_fuel_requirement)