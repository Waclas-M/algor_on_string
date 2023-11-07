import unittest
import palindrom_anagram
import ONP
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
    def test_ONP(self):
        self.assertEqual(ONP.ONP("4*6+3"),"46*3+")
        self.assertEqual(ONP.ONP("(3+4)+15/3"),"34+153/+")
        self.assertEqual(ONP.ONP("(2+3)-(3+4)"),"23+34+-")


