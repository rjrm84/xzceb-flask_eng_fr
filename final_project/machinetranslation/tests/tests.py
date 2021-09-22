import unittest
from translator import frenchToEnglish
from translator import englishToFrench


class TestenglishtoFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(Hello), Bonjour) # Test case 1
        self.assertEqual(englishToFrench(Water), Eau) # Test case 2

class TestfrenchtoEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToEnglish(Bonjour), Hello) # Test case 3
        self.assertEqual(frenchToEnglish(Eau), Water) # Test case 4

