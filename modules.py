import random

def get_def_and_pop(word_list, word_dict):
	'''this function will return the key-value pair where key is the word and defination is the value  as a tuple
	(word, definition)'''
	random_index = random.randrange(len(word_list))
	word = word_list.pop(random_index)
	definition = word_dict.get(word)
	return word,definition

def split_word_definition(rawstring):
	'''split the word and definition'''
	word, definition = rawstring.split(',',1)
	return word, definition

def read_file():
	'''read file of words and definition'''
	fh = open("Vocabulary_list.csv", "r")
	wd_list = fh.readlines()
	return wd_list

def custom_file(wd_list):
	'''create file of words and definition without duplicate entries'''
	wd_set = set(wd_list)
	fh = open("Vocabulary_set.csv", "w")
	fh.writelines(wd_set)
	return wd_set

def creating_dictionary(wd_set):
	'''creating dictionary with key as word and value as definition'''
	word_dict = dict()
	for rawstring in wd_set:
		word, definition = split_word_definition(rawstring)
		word_dict[word] = definition
	return word_dict
    