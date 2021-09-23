import unittest
from machinetranslation import translator
from translator import englishToFrench
from translator import frenchToEnglish

class TestTranslator(unittest.TestCase):
    # test function 
    def test_englishToFrench(self):
        self.assertIsNotNone(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
    def test_frenchToEnglish(self):
        self.assertIsNotNone(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
  
if __name__ == '__main__':
    unittest.main()