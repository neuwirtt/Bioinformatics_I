
def HammingDistance(p,q):
	HammingDistance = 0
	for i in range(0,len(p)):
		if p[i] != q[i]:
			HammingDistance = HammingDistance + 1
	return HammingDistance


def PatternCount (Text, Pattern, d):
	position = []
	limit = (len(Text)-len(Pattern))
	for i in range(0,limit + 1):
		mismatch = HammingDistance(Pattern,Text[i:(len(Pattern)+i)])
		if mismatch <= d:
			position.append(i)
	return position




with open("dataset_9_6.txt","r") as file1:
	data = file1.readlines()
	pattern = data[0].strip()
	string = data[1].strip()
	d = int(data[2])


Positions = PatternCount(string,pattern,d)
Count = len(Positions)
print(*Positions,sep=" ")
print(Count)