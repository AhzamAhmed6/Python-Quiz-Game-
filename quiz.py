import random
from modules import *

# STARTING OF OUR PROGRAM

wd_list = read_file()
wd_set = custom_file(wd_list)
word_dict = creating_dictionary(wd_set)
#loop for creating quiz question with multiple choices
def quiz():
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
		print("-------------")
		#printing the choices using for each loop
		for idx, choice in enumerate(choice_list):
			#printing index
			print(idx+1, choice)
		#getting input from the user
		choice = int(input("Enter 1,2,3,4; 0 to exit: "))
		#if user selects the correct choice
		if choice_list[choice-1] == definition:
			print("Correct!\n")
		#if user wants to exit
		elif choice == 0:
			exit(0)
		#if user selects the wrong choice
		else:
			print("Incorrect You lose this\n")

quiz()
