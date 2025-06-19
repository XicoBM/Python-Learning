
def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    return f"{max(num_list)} {min(num_list)}"

def high_and_low_v2(numbers):
    num_list = [int(num) for num in numbers.split()]
    return f"{max(num_list)} {min(num_list)}"

assert high_and_low_v2("1 2 3") == "3 1"
assert high_and_low_v2("1 2 3 4 5") == "5 1"
assert high_and_low_v2("1 2 -3 4 5") == "5 -3"
assert high_and_low_v2("1 9 3 4 -5") == "9 -5"
assert high_and_low_v2("1 2 3 4 5 6 7 8 9") == "9 1"
assert high_and_low_v2("1 2 3 4 5 6 7 8 9 10") == "10 1"

assert high_and_low("1 2 3 4 5") == "5 1"
assert high_and_low("1 2 -3 4 5") == "5 -3"
assert high_and_low("1 9 3 4 -5") == "9 -5"
assert high_and_low("1 2 3") == "3 1"
assert high_and_low("1 2 3 4 5 6 7 8 9") == "9 1"
assert high_and_low("1 2 3 4 5 6 7 8 9 10") == "10 1"           
assert high_and_low("1 2 3 4 5 6 7 8 9 10 11") == "11 1"
