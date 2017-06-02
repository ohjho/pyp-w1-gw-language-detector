# -*- coding: utf-8 -*-

def detect_language(text, languages):
    """Returns the detected language of given text."""

    count = {}
    for language in languages:
        matches = (len(set(text.split(' ')) & set(language['common_words'])))
        count[language['name']] = matches
    
    return max(count, key=count.get)
    
    
