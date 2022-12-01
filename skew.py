def skew(String):
	matrix = {}
	skew = 0
	index = 0
	matrix[index] = skew
	for base in String:
		index = index + 1
		if base == "G":
			skew = skew + 1
			matrix[index] = skew
		elif base == "C":
			skew = skew - 1
			matrix[index] = skew
		else:
			skew = skew + 0
			matrix[index] = skew
	return matrix

def minimum(matrix):
	minimum_value = min(matrix.values())
	potential_ori = []
	for index,value in matrix.items():
		if value == minimum_value:
			potential_ori.append(index)
	return potential_ori


def maximum(matrix):
	maximum_value = max(matrix.values())
	potential_ori = []
	for index,value in matrix.items():
		if value == maximum_value:
			potential_ori.append(index)
	return potential_ori


with open("dataset_7_10.txt","r") as file:
	String = file.read()

compute = skew(String)


potential_ori = maximum(compute)


print(*potential_ori, sep=" ")
