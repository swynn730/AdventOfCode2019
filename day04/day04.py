# :REAL DATA FOR PART 1 AND 2:
puzzle_input = "197487-673251"
minimum_puzzle_input_range, maximum_puzzle_input_range = puzzle_input.split("-")

# :TEST DATA PART 1:
# 122345 valid
# 111111 valid
# 223450 not valid
# 123789 not valid
# The amount of valid passwords should be 2.
# passwords = ["122345", "111111", "223450", "123789"]

# :TEST DATA PART 2:
# 112233 valid
# 123444 not valid
# 111122 valid
# 111222 not valid
# 222122 not valid
# 112211 valid
# 123455 valid
# 555233 valid
# 552333 valid
# 123456 not valid
# 112233 valid
# The amount of valid passwords should be 4 when running this data against all of the tests. 
# When just running this data against the 'are_two_adjacent_digits_same_but_not_apart_of_a_larger_group' function the number of valid passwords will be 7.
# passwords = ["112233", "123444", "111122", "111222", "222122", "112211", "123455", "555233", "552333", "123456", "112233"]

def is_six_digit_number(number):
    """
    It is a six-digit number.
    """
    return len(str(number)) >= 6

def is_within_puzzle_input_range(number, low_range, high_range):
    """
    The value is within the range given in your puzzle input.
    """
    return int(number) >= int(low_range) and int(number) <= int(high_range)

def are_two_adjacent_digits_same(number):
    """
    Two adjacent digits are the same (like 22 in 122345).
    """
    number = list(str(number))
    while len(number) > 1:
        if int(number[-1]) == int(number[-2]):
            return True
        else:
            del(number[-1])
    return False

def are_digits_increasing_or_staying_the_same(number):
    """
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    """
    number = list(str(number))
    for index, digit in enumerate(number):
        if index == 0 or int(digit) >= int(number[index-1]):
            continue
        else:
            return False
    return True

# Use this function for part 2 only.
def are_two_adjacent_digits_same_but_not_apart_of_a_larger_group(number):
    """
    Two adjacent digits are the same (like 22 in 122345) but not part of a larger group of matching digits.
    Example:
        112233 valid.
        123444 not valid.
    """
    number = list(str(number))
    adjacent_matches = []
    while len(number) > 1:
        # Everytime we come across a match, store it off.
        if int(number[-1]) == int(number[-2]):
            adjacent_matches.append([int(number[-1]), int(number[-2])])
        del(number[-1])
    # If there is just one match there is no way it's apart of a larger group.
    # Example: 123455 -> [[5, 5]].
    if len(adjacent_matches) == 1:
        return True
    # If there are multiple matches and the first two are unique there is no way it's apart of a larger group.
    # Example: 555233 -> [[3, 3], [5, 5], [5, 5]].
    elif len(adjacent_matches) >= 2 and (adjacent_matches[0] != adjacent_matches[1]):
        return True
    # If there are multiple matches and the last two are unique there is no way it's apart of a larger group.
    # Example: 552333 -> [[3, 3], [3, 3], [5, 5]].
    elif len(adjacent_matches) >= 2 and (adjacent_matches[-2] != adjacent_matches[-1]):
        return True
    # This covers any other scenario, meaning there are no matches or everything matches with each other, which means it's apart of a larger group.
    # Example: 123444 -> [[4, 4], [4, 4]].
    # Example: 123456 -> [].
    return False

valid_passwords_count = 0

# :TEST DATA PART 1:
# for password in passwords:
#     test_0 = is_six_digit_number(password)
#     test_1 = is_within_puzzle_input_range(password, 0, 100000000)
#     test_2 = are_two_adjacent_digits_same(password)
#     test_3 = are_digits_increasing_or_staying_the_same(password)
#     if test_0 and test_1 and test_2 and test_3:
#         valid_passwords_count +=1

# Part 1
# Answer: 1640
# :REAL DATA PART 1:
# for password in range(int(minimum_puzzle_input_range), (int(maximum_puzzle_input_range) + 1)):
#     test_0 = is_six_digit_number(password)
#     test_1 = is_within_puzzle_input_range(password, int(minimum_puzzle_input_range), int(maximum_puzzle_input_range))
#     test_2 = are_two_adjacent_digits_same(password)
#     test_3 = are_digits_increasing_or_staying_the_same(password)
#     if test_0 and test_1 and test_2 and test_3:
#         valid_passwords_count +=1

# :TEST DATA PART 2:
# for password in passwords:
#     test_0 = is_six_digit_number(password)
#     test_1 = is_within_puzzle_input_range(password, 0, 100000000)
#     test_2 = are_two_adjacent_digits_same(password)
#     test_3 = are_digits_increasing_or_staying_the_same(password)
#     test_4 = are_two_adjacent_digits_same_but_not_apart_of_a_larger_group(password)
#     if test_0 and test_1 and test_2 and test_3 and test_4:
#         valid_passwords_count +=1

# Part 2
# Answer: 1126
# :REAL DATA PART 2:
for password in range(int(minimum_puzzle_input_range), (int(maximum_puzzle_input_range) + 1)):
    test_0 = is_six_digit_number(password)
    test_1 = is_within_puzzle_input_range(password, int(minimum_puzzle_input_range), int(maximum_puzzle_input_range))
    test_2 = are_two_adjacent_digits_same(password)
    test_3 = are_digits_increasing_or_staying_the_same(password)
    test_4 = are_two_adjacent_digits_same_but_not_apart_of_a_larger_group(password)
    if test_0 and test_1 and test_2 and test_3 and test_4:
        valid_passwords_count +=1

print(valid_passwords_count)