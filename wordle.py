#!/usr/bin/env python3.7
import re

def main():
	words_file = open("words", "r")
	words_list = words_file.read().lower().splitlines()
	# print(words_list)

	contains = input("Enter Letter to included: ")
	excludes = input("Enter Letter to exclude: ")
	known_position = input("Enter known position of Letters (format: LETTER-POSITION) (seperate by space): ").split(' ')
	wrong_position = input("Enter known letter wrong positions (format: LETTER-POSITION) (seperate by space): ").split(' ')

	position_list = ['.']*5
	wrong_position_list = ['.']*5

	if known_position[0] != '':
		for pair in known_position:
			letter = pair.split('-')[0]
			position = int(pair.split('-')[1])-1

			position_list[position] = letter

	position_regex = "".join(position_list)
	# print(position_regex)

	if wrong_position[0] != '': 
		for pair in wrong_position:
			letter = pair.split('-')[0]
			position = int(pair.split('-')[1])-1

			if wrong_position_list[position] != '.':
				wrong_position_list[position] += letter
			else:
				wrong_position_list[position] = letter

		for i in range(0, 5):
			if wrong_position_list[i] != '.':
				wrong_position_list[i] = f'[^{wrong_position_list[i]}]'
	

	wrong_position_regex = "".join(wrong_position_list)
	# print(wrong_position_regex)


	contains_list = [word for word in words_list if all(letter in word for letter in contains)]
	contains_and_exclude_list = [word for word in contains_list if all(letter not in word for letter in excludes)]
	
	r = re.compile(position_regex)
	almost_final_word_list = list(filter(r.match, contains_and_exclude_list))

	r2 = re.compile(wrong_position_regex)
	final_words_list = list(filter(r2.match, almost_final_word_list))

	print(final_words_list)

if __name__ == '__main__':
	main()