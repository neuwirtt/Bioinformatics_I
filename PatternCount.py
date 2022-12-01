

def PatternCount (Text, Pattern):
	count = 0
	limit = (len(Text)-len(Pattern))
	for i in range(0,limit + 1):
		if Pattern == Text[i:(len(Pattern)+i)]:
			count = count + 1
	return count


with open("dataset_2_6.txt","r") as file1:
	Text = file1.read()

with open("Pattern.txt","r") as file2:
	Pattern = file2.read()

print(PatternCount(Text, Pattern))