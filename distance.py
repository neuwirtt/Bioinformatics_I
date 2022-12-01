


def HammingDistance(p,q):
	HammingDistance = 0
	for i in range(0,len(p)):
		if p[i] != q[i]:
			HammingDistance = HammingDistance + 1
	return HammingDistance

	
def DistanceBetweenPatternAndStrings(Pattern, DNA):
	k = len(Pattern)
	distance = 0
	for sequence in DNA:
		Hamming_distance = float('inf')
		for i in range(len(sequence)-k+1):
			if Hamming_distance > HammingDistance(Pattern, sequence[i:i+k]):
				Hamming_distance = HammingDistance(Pattern, sequence[i:i+k])
		distance += Hamming_distance
	return distance

with open("dataset_5164_1.txt","r") as file:
	data = file.readlines()
	Pattern = data[0].strip()
	DNA = data[1].strip().split(" ")

distance = DistanceBetweenPatternAndStrings(Pattern, DNA)
print(distance)