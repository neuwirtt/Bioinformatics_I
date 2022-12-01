def PatternCount (Text, Pattern):
	position = []
	limit = (len(Text)-len(Pattern))
	for i in range(0,limit + 1):
		if Pattern == Text[i:(len(Pattern)+i)]:
			position.append(i)
	return position


with open("input_1.txt","r") as file1:
	Text = file1.read()

Pattern = input("Input pattern: ")

Count = PatternCount(Text, Pattern)

print(*Count,sep=" ")