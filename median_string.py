from itertools import product


def HammingDistance(p,q):
    HammingDistance = 0
    for i in range(0,len(p)):
        if p[i] != q[i]:
            HammingDistance = HammingDistance + 1
    return HammingDistance


def median_string(k, dna_list):
    # Initialize the best pattern score as one greater than the maximum possible score.
    best_score = k*len(dna_list) + 1

    # Check the scores of all k-mers.
    for pattern in product('ACGT', repeat=k):
        current_score = sum([motif_score(''.join(pattern), dna) for dna in dna_list])
        if current_score < best_score:
            best_score = current_score
            best_pattern = ''.join(pattern)

    return best_pattern


def motif_score(pattern, motif):
    '''Returns the score of d(pattern, motif).'''
    return min([HammingDistance(motif[i:i+len(pattern)], pattern) for i in range(len(motif)-len(pattern)+1)])


with open("test_05.txt","r") as file:
    data = file.readlines()
    k = int(data[0].strip())
    DNA = data[1].strip().split(" ")

median = median_string(k, DNA)
print(median)