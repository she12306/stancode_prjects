"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: The integer whose maximum value is to be calculated.
	:return: The maximum value returned by the helper.
	"""
	counter = [0]
	if n < 0:
		n *= -1
	return find_largest_digit_helper(n, 0, counter)


def find_largest_digit_helper(n, maximum, counter):
	counter[0] += 1
	if n < 10:  # If n < 0, Big O will be "the number of bits + 1".
		if n > maximum:
			maximum = n
		return maximum, counter
	else:
		if n % 10 > maximum:
			maximum = n % 10
		return find_largest_digit_helper(int(n / 10), maximum, counter)


if __name__ == '__main__':
	main()
