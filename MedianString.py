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
		for i in range(0,len(sequence)-k+1):
			if Hamming_distance > HammingDistance(Pattern, sequence[i:i+k]):
				Hamming_distance = HammingDistance(Pattern, sequence[i:i+k])
		distance += Hamming_distance
	return distance


def MedianString (DNA, k):
	kmer_list = []
	for sequence in DNA:
		for i in range(0,len(sequence)-k+1):
			pattern = sequence[i:i+k]
			if pattern not in kmer_list:
				kmer_list.append(pattern)
	distance  = float('inf')
	for kmer in kmer_list:
		d = DistanceBetweenPatternAndStrings(kmer, DNA)
		if distance > d:
			distance = d
			median = kmer
	return median


with open("test_05.txt","r") as file:
	data = file.readlines()
	k = int(data[0].strip())
	DNA = data[1].strip().split(" ")

median = MedianString (DNA, k)
print(median)