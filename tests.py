"""
Testing translator.py module
"""
import unittest

from translator import englishtofrench, englishtogerman

class TestEnToFr(unittest.TestCase):
    """
    Testing TestEnToFr // english to french
    """
    def test_hello(self):
        """
        testing hello with French
        """
        self.assertEqual(englishtofrench("hello"), "Bonjour")
    def test_other(self):
        """
        testing nice to meet you with French
        """
        self.assertEqual(englishtofrench("nice to meet you"), "Gentiez de vous rencontrer")
    def test_null(self):
        """
        testing null
        """
        with self.assertRaises(Exception) as context:
            englishtofrench(None)
        self.assertTrue('ApiException' in context.exception)

class TestEnToDe(unittest.TestCase):
    """
    Testing TestEnToDe // english to German
    """
    def test_hello(self):
        """
        testing hello with German
        """
        self.assertEqual(englishtogerman("hello"), "Hallo")
    def test_other(self):
        """
        testing nice to meet you with German
        """
        self.assertEqual(englishtogerman("nice to meet you"), "nett, dich zu treffen,")
    def test_null(self):
        """
        testing null
        """
        with self.assertRaises(Exception) as context:
            englishtogerman(None)
        self.assertTrue('ApiException' in context.exception)
        
unittest.main()
