"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():
	"""
	Roll the dice until the same side appears multiple times in a row.
	'Number of runs' can determine the number of consecutive repetitions.
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	repeat = 0

	# 1st roll
	roll = r.randint(1, 2)
	ans = str(roll)

	while True:
		roll = r.randint(1, 2)
		ans += str(roll)

		# 2nd roll: Same as the latter.
		if len(ans) == 2:
			if ans[0] == ans[1]:
				repeat += 1
		# Continuous roll: Same as the latter, different from the former.
		else:
			if ans[len(ans)-2] is ans[len(ans)-1] and ans[len(ans)-2] is not ans[len(ans)-3]:
				repeat += 1
		if repeat == num_run:
			break

	# print result
	result = ''
	for point in ans:
		if point is '1':
			result += 'H'
		elif point is '2':
			result += 'T'
	print(result)



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
