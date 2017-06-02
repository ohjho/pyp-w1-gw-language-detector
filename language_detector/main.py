# -*- coding: utf-8 -*-
from __future__ import print_function
from languages import LANGUAGES
from collections import Counter


"""This is the entry point of the program."""

def counter_example(a_dictionary):
    
    c = Counter(a_dictionary.split(' '))
    print(c.most_common())


def detect_language(text, languages):
    """Returns the detected language of given text."""

    
    count = {}
    for language in languages:
        matches = (len(set(text.split(' ')) & set(language['common_words'])))
        count[language['name']] = matches
    
    return max(count, key=count.get)
    
    

if __name__ == '__main__':
    example = """Lionel Andrés 'Leo' Messi is an Argentine professional footballer
            who plays as a forward for Spanish club FC Barcelona and the
            Argentina national team. Often considered the best player in the
            world and rated by many in the sport as the greatest of all time,
            Messi is the only football player in history to win five FIFA
            Ballons, four of which he won consecutively, and the first player
            to win three European Golden Shoes."""
    
    counter_example(example)