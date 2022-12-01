import math
import random


class Bioinformatics(object):


    def __init__(self):
        pass

    def randomMotifs(self):
        randomizedMotifs=["TGA","GTT","GAA","TGT"]
        return randomizedMotifs

    def countWithPseudocounts(self,motifs):
        k = len(motifs[0])
        count = {}
        for symbol in "ACGT":
            count[symbol]=[]
            for j in range(k):
                count[symbol].append(1) # to create the lapalce pseudocoutns intead of initializing with zeroes I do it with ones
        t = len(motifs)
        for i in range(t):
            for j in range(k):
                symbol = motifs[i][j]
                count[symbol][j] += 1
        return count

    def profileWithPseudocounts(self,motifs):
        countMatrix = self.countWithPseudocounts(motifs)
        profileMatrix = {}
        k = len(motifs[0]) # number of columns
        t = len(motifs) # number of rows
        totatDivCount = 0 # laPlace
        for symbol in "ACGT":
            totatDivCount += countMatrix[symbol][0]
            profileMatrix[symbol]=[]
            for j in range(k):
                profileMatrix[symbol].append(0)
        for symbol in "ACGT":
            for j in range(k):
                profileMatrix[symbol][j]=countMatrix[symbol][j]/totatDivCount
        return profileMatrix

    def kmerProb(self,kmer,profileMatrix):
        k = len(kmer)
        probability = 1
        for j in range(k):
            symbol = kmer[j]
            probability *= profileMatrix[symbol][j]
        return probability

    def mostProbableKmer(self,dna,k,profileMatrix):
        max = 0
        maxKmer =dna[0:k] # return first kmer if probability for all is zero
        totalLenght=len(dna)
        for i in range(len(dna)-k+1):
            kmer = dna[i:i+k]
            prob = self.kmerProb(kmer,profileMatrix)
            if prob > max:
                max = prob
                maxKmer = kmer
        return maxKmer

    def motif(self, profileMatrix, dna,k=4):
        mostProbableKmerDna = []
        for row in dna:
            mostProbableKmerDna.append(self.mostProbableKmer(row,k,profileMatrix))
        return mostProbableKmerDna

    def consensus(self,motifs):
        consensusString = ""
        k = len(motifs[0])  # number of columns
        countMatrix = self.countWithPseudocounts(motifs)
        for j in range(k):
            m = 0
            frequentSymbol = ""
            for symbol in "ACGT":
                if countMatrix[symbol][j]> m:
                    m = countMatrix[symbol][j]
                    frequentSymbol = symbol
            consensusString += frequentSymbol
        return consensusString

    def scorewithPseudocounts(self,motifs):
        consensusString = self.consensus(motifs)
        countMatrix = self.countWithPseudocounts(motifs)
        score = 0
        k = len(motifs[0])
        for symbol in "ACGT":
            for j in range (k):
                if symbol != consensusString[j]:
                    score += countMatrix[symbol][j]
        return score

    def randomizedMotifSearch(self, dna, k, t):
        m = self.randomMotifs()
        bestMotifs = m
        while True:
            profile = self.profileWithPseudocounts(m)
            m = self.motif(profile, dna, k)
            if self.scorewithPseudocounts(m) < self.scorewithPseudocounts(bestMotifs):
                bestMotifs = m
            else:
                return bestMotifs

    def randomizedMotifSearchNtimes(self,dna,k,t,n):
        m= self.randomMotifs()
        bestMotifs = m
        for i in range(0,n):
            m = self.randomizedMotifSearch(dna,k,t)
            if self.scorewithPseudocounts(m) < self.scorewithPseudocounts(bestMotifs):
                bestMotifs = m[:]
        return bestMotifs


def main():

    bio = Bioinformatics()
    filename = 'datatest.txt'
    with open(filename, "r") as dataset:
        data = []
        for line in dataset:
            data.append(line.strip())
        k_string,t_string = data[0].split()
        k = int(k_string)
        t = int(t_string)
        dna_sequences = data[1].strip().split() # several motifs
        n = 1
        # print (dna_sequences,k,t,n)
        list = bio.randomizedMotifSearchNtimes(dna_sequences,k,t,n)
        print(*list) # separate the elements with one space only (using *
    # ---------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()