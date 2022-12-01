
from itertools import combinations, product
from functools import reduce

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


def MotifEnumeration(DNA_set,k,d):
	motif_sets = [{kmer for i in range(0,len(dna)-k+1) for kmer in kmer_mismatches(dna[i:i+k], d)} for dna in DNA_set]

	return sorted(list(reduce(lambda a,b: a & b, motif_sets)))


with open("input_1.txt","r") as file:
	data = file.readlines()
	DNA_set = data[1].strip().split()
	k, d = data[0].strip().split()

print(k,d)
print(DNA_set)

Motifs = MotifEnumeration(DNA_set,int(k),int(d))

print(*Motifs,sep=" ")