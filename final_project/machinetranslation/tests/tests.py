import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french("none"), '') # test none value from english to french
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # test hello to bonjour translation
        

class TestfrenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertNotEqual(french_to_english("none"), '') # test none value from french to english
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test bonjour to hello translation

unittest.main()

