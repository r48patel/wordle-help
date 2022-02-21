#!/usr/bin/env python3.7
import re


def get_possible_word_list(contains, excludes, known_position, wrong_position):
	# Read files with all the words
	words_file = open("words", "r")
	words_list = words_file.read().lower().splitlines()

	# Filter out words that doesn't contain known letters
	contains_list = [word for word in words_list if all(letter in word for letter in contains.lower())]

	# Filter out words from above that contains wrong letters
	contains_and_exclude_list = [word for word in contains_list if all(letter not in word for letter in excludes.lower())]

	# Create a regex for known letters position and filter the above list with it.
	position_list = ['.']*5
	if known_position:
		for pair in known_position.lower().split(' '):
			if '-' in pair:
				letter = pair.split('-')[0]
				position = int(pair.split('-')[1])-1
			else:
				letter = pair[0]
				position = int(pair[1])-1

			position_list[position] = letter

	position_regex = "".join(position_list)
	r = re.compile(position_regex)
	almost_final_word_list = list(filter(r.match, contains_and_exclude_list))

	# Create a regex with known letters wrong position and filter the above list.
	wrong_position_list = ['.']*5
	if wrong_position:
		for pair in wrong_position.lower().split(' '):
			if '-' in pair:
				letter = pair.split('-')[0]
				position = int(pair.split('-')[1])-1
			else:
				letter = pair[0]
				position = int(pair[1])-1

			if wrong_position_list[position] != '.':
				wrong_position_list[position] += letter
			else:
				wrong_position_list[position] = letter

		for i in range(0, 5):
			if wrong_position_list[i] != '.':
				wrong_position_list[i] = f'[^{wrong_position_list[i]}]'

	wrong_position_regex = "".join(wrong_position_list)
	r2 = re.compile(wrong_position_regex)
	final_words_list = list(filter(r2.match, almost_final_word_list))

	return final_words_list


def main():
	contains = input("Enter Letter to included: ")
	excludes = input("Enter Letter to exclude: ")
	known_position = input("Enter known position of Letters separate by space (ex: s3 a1) : ")
	wrong_position = input("Enter known letter wrong positions separate by space (ex: t1 u2): ")

	print(get_possible_word_list(contains, excludes, known_position, wrong_position))


if __name__ == '__main__':
	main()
