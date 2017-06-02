# -*- coding: utf-8 -*-
from __future__ import print_function
from languages import LANGUAGES

"""This is the entry point of the program."""

def word_counts(str_text, list_word):
    """a helper function"""
    wcount=0
    for word in str_text.split():
        if word in list_word:
            wcount+=1
    return wcount

def detect_language_jho(text, languages):
    """Returns the detected language of given text."""
    output=""
    word_count = []
    for lang in languages:
        icount= word_counts(text,lang['common_words'])
        word_count.append(icount)
    
    for i, item in enumerate(word_count):
        if item==max(word_count):
            output= languages[i]['name']
    
    return output

if __name__ == '__main__':
    user_text = """
            Lionel Andrés 'Leo' Messi is an Argentine professional footballer
            who plays as a forward for Spanish club FC Barcelona and the
            Argentina national team. Often considered the best player in the
            world and rated by many in the sport as the greatest of all time,
            Messi is the only football player in history to win five FIFA
            Ballons, four of which he won consecutively, and the first player
            to win three European Golden Shoes.
        """
    print(detect_language_jho(user_text, LANGUAGES))