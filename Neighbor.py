from itertools import combinations, product

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

Neighborhood = kmer_mismatches("ACGT",3)

print(len(Neighborhood))

print(*Neighborhood,sep=" ")