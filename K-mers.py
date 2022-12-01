

def FrequencyTable (Text,k):
	freqMap = {}
	n = len(Text)
	limit = n-k
	for i in range(0,(limit+1)):
		Pattern = Text[i:(k+i)]
		if freqMap.get(Pattern) is None:
			freqMap[Pattern] = 1
		else:
			freqMap[Pattern] =  freqMap[Pattern] + 1
	return freqMap


def FrequentWords (freqMap):
	frequent_patterns = []
	m = max(freqMap.values())
	for pattern, freq in freqMap.items():
		if freqMap[pattern] == m:
			frequent_patterns.append(pattern)
	return frequent_patterns


with open("dataset_2_13.txt") as file:
	Text = file.read()

k = int(input("Input k: "))



freqMap = FrequencyTable(Text,k)

print(FrequentWords(freqMap))

