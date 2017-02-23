import HMM

from nltk.corpus import cmudict
d = cmudict.dict()
def nsyl(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]

file = open('project2data/shakespeare.txt')
rawsonnets = file.readlines()
sonnets = []
for item in rawsonnets:
	if item != '\n' and item[-2] not in ['0','1','2','3','4','5','6','7','8','9']:
		sonnets.append(item)

punctuation = [',', ';', ':', '.', '(', ')', '!']

for i in range(len(sonnets)):
	sonnets[i] = sonnets[i].split()
	for j in range(len(sonnets[i])):
		for k in punctuation:
			if k in sonnets[i][j]:
				sonnets[i][j] = sonnets[i][j].replace(k, '')
	sonnets[i][0] = sonnets[i][0].lower()

hash1 = {}
hash2 = {}
z = 0

hashedsonnets = [[0 for i in range(len(sonnets[j]))] for j in range(len(sonnets))]

for i in range(len(sonnets)):
	for j in range(len(sonnets[i])):
		if sonnets[i][j] not in hash1:
			hash1[sonnets[i][j]] = z
			hash2[z] = sonnets[i][j]
			z += 1
		hashedsonnets[i][j] = hash1[sonnets[i][j]]

print hashedsonnets

hmm = HMM.unsupervised_HMM(hashedsonnets, 7, 50)

for i in range(20):
	emission =  hmm.generate_emission(10)
	string = ""
	for j in emission:
		string += hash2[int(i)]
		string += " "
	print string