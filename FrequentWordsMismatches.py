
def ImmediateNeighbors(Pattern):
	Neighborhood = set()
	Neighborhood.add(Pattern)
	nucleotides = ["A","C","G","T"]
	for i in range(0,len(Pattern)):
		symbol = Pattern[i]
		for nucleotide in nucleotides:
			if symbol != nucleotide:
				Neighbor = Pattern[:i] + nucleotide + Pattern[(i+1):]
				Neighborhood.add(Neighbor)
	return Neighborhood


def IterativeNeighbors(Pattern, d):
	Neighborhood = set()
	Neighborhood.add(Pattern)
	for j in range(0,d):
		for String in Neighborhood:
			Neighborhood = Neighborhood.union(ImmediateNeighbors(Pattern))
	return Neighborhood


def FrequentWords (string,k,d):
	frequent_patterns = []
	freqMap = {}
	n = len(string)
	for i in range(0,((n-k)+1)):
		Pattern = string[i:(k+i)]
		neighborhood = list(IterativeNeighbors(Pattern,d))
		for j in range(0,len(neighborhood)):
			neighbor = neighborhood[j]
			if freqMap.get(neighbor) is None:
				freqMap[neighbor] = 1
			else:
				freqMap[neighbor] = freqMap[neighbor] + 1
	m = max(freqMap.values())
	for pattern, freq in freqMap.items():
		if freqMap[pattern] == m:
			frequent_patterns.append(pattern)
	return frequent_patterns


with open("dataset_9_9.txt") as file:
	data = file.readlines()
	string = data[0].strip()
	numbers = data[1].split(" ")
Patterns = FrequentWords(string,int(numbers[0]),int(numbers[1]))
print(*Patterns,sep=" ")
