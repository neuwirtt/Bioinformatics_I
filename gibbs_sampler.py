import math
import random

class Bioinformatics(object):


    def __init__(self):
        pass

    def randomMotifs(self,dna,k,t):
        randomizedMotifs=[]
        for row in dna:
            startNum = random.randint(0,len(row)-1)
            if startNum + k < len(row):
                randomizedMotifs.append(row[startNum:startNum+k])
            else:
                randomizedMotifs.append(row[startNum-k:startNum])
        return randomizedMotifs

    def score(self,motifs):
        consensusString = self.consensus(motifs)
        countMatrix = self.count(motifs)
        score = 0
        k = len(motifs[0])
        for symbol in "ACGT":
            for j in range (k):
                if symbol != consensusString[j]:
                    score += countMatrix[symbol][j]
        return score


    def cloning(self, li1):
    	li_copy = li1[:]
    	return li_copy

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


    def normalize(self,probabilities):
        sum = 0
        for element in probabilities.values():
            sum += element
        for element2 in probabilities.keys():
            probabilities[element2]=probabilities[element2]/sum
        return probabilities
    
    def weightedDie(self,probabilities):
        kmer = ''
        number = random.uniform(0,1)
        acum = 0
        for element in probabilities.keys():
            if number >= acum and number < acum + probabilities[element]:
                kmer = element
            acum += probabilities[element]
        return kmer
    
    def profileGeneratedString(self, Text, profile, k):
        n = len(Text)
        probabilities = {}
        probabilities_normalized = {}
        probabilities_weighted = {}
        for i in range(0,n-k+1):
            kmer = Text[i:i+k]
            probabilities[kmer] = self.kmerProb(kmer,profile)
        probabilities_normalized = self.normalize(probabilities)
        string_probabilities_weighted = self.weightedDie(probabilities_normalized)
        return string_probabilities_weighted


    def gibbsSampler(self,dna, k, t, N):
        bestMotifs = []
        motifs = self.randomMotifs(dna,k,t)
        bestMotifs = motifs
        for j in range(1, N):
            i = random.randint(0, t-1)
            motifs_without_i= self.cloning(motifs)
            motifs_selected = motifs[i]
            motifs_without_i.pop(i)
            profile = self.profileWithPseudocounts(motifs_without_i)
            dna_i = dna[i]
            kmer_profile_weighted = self.profileGeneratedString(dna_i,profile,k)
            motifs.pop(i) # it is more clear to use an auxliary list motifs_without_i for debugging
            motifs.insert(i, kmer_profile_weighted)
            if self.score(motifs) < self.score(bestMotifs):
                bestMotifs = motifs
        return bestMotifs


    def gibbsSamplerRepeatXtimes(self,dna,k,t,N,x):
        motifs = self.randomMotifs(dna,k,t)
        bestMotifs = motifs
        for i in range(0,x):
            m = self.gibbsSampler(dna,k,t,N)
            if self.score(m) < self.score(bestMotifs):
                bestMotifs = m
        return bestMotifs


def main():

    bio = Bioinformatics()

    filename = 'input_1.txt'
    with open(filename, "r") as dataset:
        data = []
        for line in dataset:
            data.append(line.strip())
        k_string,t_string,N_string = data[0].split()
        k = int(k_string)
        t = int(t_string)
        N = int(N_string)
        dna_sequences = data[1].strip().split() # several motifs
        x = 20
        # print (dna_sequences,k,t,n)
        list = bio.gibbsSamplerRepeatXtimes(dna_sequences,k,t,N,x)
        print(*list) # separate the elements with one space only (using *)


if __name__ == "__main__":
    main()