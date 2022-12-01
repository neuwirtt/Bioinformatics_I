def MostProbableProfile(DNA,k,Profile):
	profile_map = {}
	for i in range(0,len(DNA)-k+1):
		profile = 1
		kmer = DNA[i:i+k]
		for j in range(0,k):
			base = kmer[j]
			position_prob = float(Profile[base][j])
			profile = profile * position_prob
		profile_map[kmer] = profile
	return profile_map


Profile = {}
with open("dataset_159_3.txt") as file:
	data = file.readlines()
	DNA = data[0].strip()
	k = int(data[1].strip())
	Profile["A"] = data[2].strip().split(" ")
	Profile["C"] = data[3].strip().split(" ")
	Profile["G"] = data[4].strip().split(" ")
	Profile["T"] = data[5].strip().split(" ")

profile_map = MostProbableProfile(DNA,k,Profile)
find_max = max(profile_map,key=profile_map.get)

print(find_max)