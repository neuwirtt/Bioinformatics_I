def ReverseComplement(String):
	ReverseComplement = ""
	for nucleotide in String:
		if nucleotide == "A":
			ReverseComplement = ReverseComplement + ("T")
		elif nucleotide == "T":
			ReverseComplement = ReverseComplement + ("A")
		elif nucleotide == "C":
			ReverseComplement = ReverseComplement + ("G")
		elif nucleotide == "G":
			ReverseComplement = ReverseComplement + ("C")
		else:
			print("Not recognised letter in string!")
			print(nucleotide)
	return ReverseComplement

String = input("Input string: ")

Complement = ReverseComplement(String)
print(Complement)