"""
Python module provides function to translate between US English and French French
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    english_to_french takes a string of english text and translates it to french
    """
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR')\
        .translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    french_to_english takes a string of french text and translates it to english
    """
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US')\
        .translate(french_text)

    return english_text
