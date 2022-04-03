import time
import random

# txt = ''
words = []

# alpha = 'The ragdyofHmlt,PincDkACISEN.spbFROBW\'?w:uLv!Y;qMUGx-QjzJKV[]Z&'

with open("cleaned.txt", "r") as f:
	for line in f.readlines():
		line = line.strip()
		for word in line.split(' '):
			words.append(word)


def main():
	print("Starting time is:", time.asctime(time.localtime( time.time() )) )
	monkey = []
	i = 0
	longest = []
	while len(monkey) < len(words):
		w = random.choice(words)
		tmp = monkey
		tmp.append(w)
		if words[i] == w:
			i += 1
			monkey = tmp
		else:
			i = 0
			monkey = []
			if len(monkey) > len(longest):
				longest = monkey
				print('Monkey got a new record!')
				print('Monkey said:')
				string = '' 
				for wrd in monkey:
					string += wrd + ' '
				print(string)
	print("Ending time is:", time.asctime( time.localtime(time.time()) ))
main()

