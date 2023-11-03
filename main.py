import unittest
import palindrom_anagram

class Test(unittest.TestCase):
    def test_palindrom(self):
        self.assertEqual(palindrom_anagram.palindrom('ala'),True)
        self.assertEqual(palindrom_anagram.palindrom('kotek'),False)
        self.assertEqual(palindrom_anagram.palindrom('anna'),True)
        self.assertEqual(palindrom_anagram.palindrom('kajak'),True)
    def test_anagram(self):
        self.assertEqual(palindrom_anagram.anagram('krab','bark'),True)
        self.assertEqual(palindrom_anagram.anagram('krab','rak'),False)
        self.assertEqual(palindrom_anagram.anagram('kot','tok'),True)
        self.assertEqual(palindrom_anagram.anagram('tok','okt'),True)

