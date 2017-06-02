# -*- coding: utf-8 -*-
from __future__ import print_function
from languages import LANGUAGES

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    
    count = {}
    for language in languages:
        matches = (len(set(text.split(' ')) & set(language['common_words'])))
        count[language['name']] = matches
    
    return max(count, key=count.get)
        
    

