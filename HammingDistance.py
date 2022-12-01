def HammingDistance(p,q):
	HammingDistance = 0
	for i in range(0,len(p)):
		if p[i] != q[i]:
			HammingDistance = HammingDistance + 1
	return HammingDistance

with open("dataset_9_3.txt","r") as file:
	lines = file.readlines()

print(HammingDistance(lines[0].strip(),lines[1].strip()))
