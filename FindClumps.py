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


def FindClumps(String,k,L,t):
	clumps = []
	n = len(String)
	for i in range(0,((n-L)+1)):
		Window = String[i:(L+i)]
		freqMap = FrequencyTable(Window,k)
		for pattern, freq  in freqMap.items():
			if freq >= t:
				if pattern not in clumps:
					clumps.append(pattern)
	return clumps


with open("E_coli.txt","r") as file:
	String = file.read()

k = int(input("Input k: "))
L = int(input("Input L: "))
t = int(input("Input t: "))

Clumps = FindClumps(String,k,L,t)

print(len(Clumps))
