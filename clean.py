
words = []

with open("hamlet.txt", "r") as f:
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		for word in line.split(' '):
			if word == '':
				continue
			words.append(word)

with open("cleaned.txt", "w") as f:
	for word in words:
		f.write(word + ' ')

