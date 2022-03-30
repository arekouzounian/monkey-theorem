import time
import random

txt = ''

alpha = 'The ragdyofHmlt,PincDkACISEN.spbFROBW\'?w:uLv!Y;qMUGx-QjzJKV[]Z&'

with open("cleaned.txt", "r") as f:
	txt = f.read().replace('\n', '')


def main():
	print("Starting time is:", time.asctime(time.localtime( time.time() )) )
	pos = 0
	l = len(txt)
	monkey = ''
	longest = ''
	while pos < l:
		c = random.choice(alpha)
		monkey += c
		if txt[pos] == c:
			pos += 1
		else:
			pos = 0
			if  len(monkey)-1 > len(longest):
				longest = monkey[:-1]
				print("Monkey failed!")
				print("Monkey's longest Hamlet so far:", "\"" + longest + "\"" , "\n")
				print("Monkey was", (float(pos)/l)*100, "% into Hamlet. Resetting...")
			monkey = ''
	print("Ending time is:", time.asctime( time.localtime(time.time()) ))


main()
