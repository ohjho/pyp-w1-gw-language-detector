# -*- coding: utf-8 -*-
from __future__ import print_function

from languages import LANGUAGES

def detect_language(text, languages):
    """Returns the detected language of given text."""
    
    count = {}
    for language in languages:
        matches = (len(set(text.split(' ')) & set(language['common_words'])))
        count[language['name']] = matches
    
    return max(count, key=count.get)
        
    

if __name__ == '__main__':
    user_text = """
            Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
            conocido como Leo Messi, es un futbolista argentino11 que juega
            como delantero en el Fútbol Club Barcelona y en la selección
            argentina, de la que es capitán. Considerado con frecuencia el
            mejor jugador del mundo y calificado en el ámbito deportivo como el
            más grande de todos los tiempos, Messi es el único futbolista en la
            historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de
            ellos en forma consecutiva– y el primero en
            recibir tres Botas de Oro.
        """
    print(detect_language(user_text, LANGUAGES))
    