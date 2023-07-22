import unittest
from '../translator' import english_to_french, french_to_english
class TestTranslations(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('dog'), 'chien')
    def test_fr_to_en(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hi')
        self.assertEqual(french_to_english('chien'), 'dog')

if __name__ == '__main__':
    unittest.main()