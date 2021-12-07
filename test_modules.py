from modules import *


def test_read_file():
    assert read_file() == wd_list


def test_custom_file():
    assert custom_file(wd_list) == wd_set


def test_creating_dictionary():
    assert creating_dictionary(wd_set) == word_dict

