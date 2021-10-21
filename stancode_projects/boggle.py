"""
File: boggle.py
Name: Heather Ou
----------------------------------------
Let's play Boggle!
"""

import time
import sys


# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_d = {}
ans_lst = []


def main():
	"""
	1. Let the user input and sort the input str (Or enter 'py boggle.py test' to test).
	2. Convert input str to dict -> {coordinate: 'letter'}.
	3. Use for loop to choose the first letter.
	4. Use recursion to append the other letters.
	"""
	start = time.time()
	####################
	s = ''
	args = sys.argv[1:]
	if not args:
		for i in range(4):
			row = input(f'{i + 1} row of letters: ')
			if not check_letters_line(row):
				print('Illegal input')
				exit()
			s += check_letters_line(row)
	else:
		if args[0] == 'test':
			r1 = 'fyct'
			r2 = 'ioma'
			r3 = 'oril'
			r4 = 'hjhu'
			s = r1 + r2 + r3 + r4

	# Convert the input letters into letter_d -> {(x, y): 'letter'}
	letter_d = {}
	for i in range(4):
		for j in range(4):
			letter_d[(i, j)] = s[i*4+j]

	# According to s, sort out dict_d
	read_dictionary(s)

	# Choose the first letter
	for i in range(4):
		for j in range(4):
			cur = str(letter_d[(i, j)])
			pass_by = [(i, j)]
			neighbor = find_neighbor(i, j)
			# Append other letters
			find_word(letter_d, cur, pass_by, neighbor)
	print(f'There are {len(ans_lst)} words in total.')

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(letter_d, cur, pass_by, neighbor):
	"""
	如果base case設為「找到word」: 找不到roomy。
	如果base case設為「找到word」, 並只延伸一個letter再搜尋: 找不到 formal和format。
	所以base case應設為「字典裡已找不到cur str開頭的word」，才能找到所有word。
	(cur str的first letter我們已經先選入了，所以不會是空字串。
	除非first letter開頭的，沒有四字以上的單字，如此則會直接進入base case。)

	:param letter_d: (dict) Coordinates(key) and letters(value).
	:param cur: (str) Current string.
	:param pass_by: (lst) Letters that have passed.
	:param neighbor: (lst) Coordinates of neighbor letters.
	"""
	if not has_prefix(cur):
		pass
	else:
		if cur in dict_d[cur[0]] and cur not in ans_lst:
			ans_lst.append(cur)
			print(f'Found: {cur}')
		# Search for words, and continue searching after finding the words, are all done here.
		for ele in neighbor:
			if ele not in pass_by:
				pass_by.append(ele)
				neighbor = find_neighbor(ele[0], ele[1])
				find_word(letter_d, cur + letter_d[ele], pass_by, neighbor)
				pass_by.pop()


def find_neighbor(x, y):
	"""
	:param x: (int) X coordinates of cur_letter
	:param y: (int) Y coordinates of cur_letter
	:return: (lst) Coordinates(Tuple) of all neighbor letters
	"""
	neighbor_lst = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			if 0 <= x + i < 4:
				if 0 <= y + j < 4:
					if not i == j == 0:  # Not itself
						neighbor_lst.append((x + i, y + j))
	return neighbor_lst


def read_dictionary(s):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list

	The dictionary only collects words starting with ch in s and the length >= 4.
	"""
	with open(FILE, 'r') as f:
		for line in f:
			for ch in s:
				word = line.strip()
				if word[0] == ch and len(word) >= 4:
					if ch not in dict_d:
						dict_d[ch] = [word]
					else:
						dict_d[ch].append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_d[sub_s[0]]:
		if word.startswith(sub_s):
			return True


def check_letters_line(row):
	"""
	Check whether the input is legal and organize it.

	:param row: (str) Input letter
	:return: (bool) Check if it is a legal string
	:return: (str) Remove spaces and convert to lowercase
	"""
	new_row = row.replace(' ', '').lower()
	if new_row.isalpha() is False or len(new_row) != 4:
		return False
	else:
		return new_row


if __name__ == '__main__':
	main()
