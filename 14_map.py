numbers = [1, 2, 3, 4]
print("numbers => ", numbers)
numbers_v2 = []
for i in numbers:
	numbers_v2.append(i + 2)
print("numbers_2 => ",numbers_v2)

#Map function
numbers_v3 = list(map(lambda i : i + 2, numbers))
print("numbers_v3 => ",numbers_v3)

# Interaction between two list - Map Function (!= dimensions => Result with minor list dimension)
numbers_4 = [5, 6, 7]
print("numbers_4 => ", numbers_4)
result_sum = list(map(lambda x, y : x + y, numbers, numbers_4))
print("result_sum => ", result_sum)

