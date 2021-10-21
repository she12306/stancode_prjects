"""
File: anagram.py
Name: Heather Ou
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
d = {}


def main():
    """
    Anagram game.
    """
    print('Welcome to stanCode "Anagram Generate" (or -1 to quit)')
    while True:
        start = time.time()
        ####################
        s = input('Find anagram for: ').lower()
        if s == EXIT:
            break
        else:
            print('Searching......')
            read_dictionary(s)
            find_anagrams(s)
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary(s):
    """
    Organize 'dictionary.txt'  into d.
    Dict_lst only selects the letters of s,
    and collects the words with these letters as the prefix and the same length as s.

    :param s: input word.
    """
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) == len(s):
                for ch in s:
                    if word[0] == ch:
                        if ch not in d:
                            d[ch] = [word]
                        else:
                            if word not in d[ch]:
                                d[ch].append(word)


def find_anagrams(s):
    """
    :param s: input word.
    """
    s_len = len(s)
    ans_lst = []
    find_anagrams_helper(s, s_len, '', '', ans_lst)
    print(f'{len(ans_lst)} anagrams: {ans_lst}')


def find_anagrams_helper(s, s_len, ans, index_str, ans_lst):
    if len(ans) == s_len:
        if ans not in ans_lst:
            if ans in d[ans[0]]:   # Search only in the lst of the specified prefix.
                ans_lst.append(ans)
                print(f'Found: {ans}')
                print('Searching......')
    else:
        for i in range(s_len):
            if str(i) not in index_str:
                if len(ans) <= 1:  # Empty string & single letter definitely can pass the check.
                    find_anagrams_helper(s, s_len, ans + s[i], index_str + str(i), ans_lst)
                else:
                    if has_prefix(ans):
                        find_anagrams_helper(s, s_len, ans + s[i], index_str + str(i), ans_lst)


def has_prefix(sub_s):
    """
    :param sub_s:
    :return: Bool
    """
    for word in d[sub_s[0]]:  # Search only in the lst of the specified prefix.
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
