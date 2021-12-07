import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

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



wd_list = read_file()
wd_set = custom_file(wd_list)
word_dict = creating_dictionary(wd_set)
def quiz():
	'''loop for creating quiz question with multiple choices'''


	print(f'''
	▀▄▀▄▀▄\t{color.YELLOW}{color.UNDERLINE}{color.BOLD}AHZAM AHMED\tCSC-20F-016{color.END}\t▀▄▀▄▀▄\n
	▀▄▀▄▀▄\t{color.BLUE}SADIQ ALI\tCSC-20F-149{color.END}\t▀▄▀▄▀▄\n
	▀▄▀▄▀▄\t{color.DARKCYAN}KAZIM ABASS\tCSC-20F-016{color.END}\t▀▄▀▄▀▄\n
	▀▄▀▄▀▄\t{color.GREEN}{color.UNDERLINE}{color.BOLD}DATA STRUCTURE AND ALGORITHM PROJECT{color.END}\t▀▄▀▄▀▄
	''')


	while True:
		wd_list = list(word_dict) #list of words
		choice_list = []#choicelist of definitions
		for x in range(4):#max 4 choices
			word, definition = get_def_and_pop(wd_list, word_dict)
			choice_list.append(definition)
		#shuffle the choices
		random.shuffle(choice_list)
		#printing a word as a quiz question
		print(word)
		print(f"{color.BOLD}-------------{color.END}")
		#printing the choices using for each loop
		for idx, choice in enumerate(choice_list):
			#printing index
			print(idx+1, choice)
		#getting input from the user
		choice = int(input(f"{color.YELLOW}{color.BOLD}Enter 1,2,3,4; 0 to exit: {color.END}"))
		#if user selects the correct choice
		if choice_list[choice-1] == definition:
			print(f"{color.GREEN}{color.BOLD}Correct!{color.END}\n")
		#if user wants to exit
		elif choice == 0:
			exit(0)
		#if user selects the wrong choice
		else:
			print(f"{color.RED}{color.BOLD}Incorrect You lose this{color.END}\n")

    