

def get_num_words(text):
	return len(text.split())

def create_character_dictionary(text):
	char_dictionary = {}

	for char in text:
		character = char.lower()
		if char_dictionary.get(character) is not None:
			char_dictionary[character] += 1
		else:
			char_dictionary.update({character: 1})

	return char_dictionary

def sorted_lists(char_dict):
	dictionary_list = []

	for key in char_dict.keys():
		new_dict = {"char": key, "num": char_dict[key]}
		dictionary_list.append(new_dict)
	
	def sorted_on(new_dict_style):
		return new_dict_style["num"]
	
	dictionary_list.sort(reverse=True, key=sorted_on)
	return dictionary_list

