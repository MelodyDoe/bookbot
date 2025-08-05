from stats import get_num_words, create_character_dictionary, sorted_lists
import sys

def main():
	args = sys.argv
	if len(args) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path = args[1]
	text = get_book_text(path)
	word_count = get_num_words(text)
	character_dictionary = create_character_dictionary(text)
	sorted_dictionary_list = sorted_lists(character_dictionary)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for pairing in sorted_dictionary_list:
		print(f"{pairing["char"]}: {pairing["num"]}")

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()


main()