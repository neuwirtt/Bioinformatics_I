

from collections import defaultdict
from itertools import combinations, product


def reverse_complement_dna(dna):
	'''Returns the reverse complement of the given DNA strand.'''
	intab = "ATCG"
	outtab = "TAGC"
	trantab = dna.maketrans(intab,outtab)
	reverse_complement = dna.translate(trantab)
	return reverse_complement[::-1]


def ImmediateNeighbors(Pattern):
	Neighborhood = list()
	Neighborhood.append(Pattern)
	nucleotides = ["A","C","G","T"]
	for i in range(0,len(Pattern)):
		symbol = Pattern[i]
		for nucleotide in nucleotides:
			if symbol != nucleotide:
				Neighbor = Pattern[:i] + nucleotide + Pattern[(i+1):]
				Neighborhood.append(Neighbor)
	print(Neighborhood)
	return Neighborhood


def IterativeNeighbors(Pattern, d):
	Neighborhood = list()
	Neighborhood.append(Pattern)
	for j in range(0,d):
		for String in Neighborhood:
			Neighborhood = Neighborhood + ImmediateNeighbors(Pattern)
	print(Neighborhood)
	return Neighborhood


def kmer_mismatches(kmer, d):
    """Returns all k-mers that are within d mismatches of the given k-mer."""
    mismatches = [kmer]  # Initialize mismatches with the k-mer itself (i.e. d=0).
    alt_bases = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
    for dist in range(1, d+1):
        for change_indices in combinations(range(0,len(kmer)), dist):
            for substitutions in product(*[alt_bases[kmer[i]] for i in change_indices]):
                new_mistmatch = list(kmer)
                for idx, sub in zip(change_indices, substitutions):
                    new_mistmatch[idx] = sub
                mismatches.append(''.join(new_mistmatch))
    return mismatches

def FrequentWords_with_mm_and_rc(string,k,d):
	"""Returns all most frequent k-mers with up to d mismatches in the dna sequence seq."""
	# Frequency analysis so we don't generate mismatches for the same k-mer more than once.
	freqMap = defaultdict(int)
	for i in range(0,((len(string)-k)+1)):
		freqMap[string[i:i+k]] += 1
		freqMap[reverse_complement_dna(string[i:k+i])] += 1

	mismatch_count = defaultdict(int)
	for pattern, freq in freqMap.items():
		for mismatch in IterativeNeighbors(pattern,d):
			mismatch_count[mismatch] += freq

	m = max(mismatch_count.values())
	frequent_patterns = sorted([pattern for pattern, count in mismatch_count.items() if count == m])
	return frequent_patterns


with open("input_3.txt") as file:
	data = file.readlines()
	string = data[0].strip()
	numbers = data[1].strip().split(" ")


print(numbers)
print(string)

Patterns = FrequentWords_with_mm_and_rc(string,int(numbers[0]),int(numbers[1]))
print(*Patterns,sep=" ")