#!C:\Users\vitor.honna\AppData\Local\Programs\Python\Python310\python.exe

from course_script_cleanup import cleanup
import unittest


class TestCleanup(unittest.TestCase):
    def test_1(self):
        testcase = '2.1.2. Title (13 SCENES)'
        expected = '2.1.2. Title -> '
        self.assertEqual(cleanup(testcase), expected)

    def test_2(self):
        testcase = '2.1.2. Title (13scenes)'
        expected = '2.1.2. Title -> '
        self.assertEqual(cleanup(testcase), expected)

    def test_3(self):
        testcase = '(SCENE 1)'
        expected = ''
        self.assertEqual(cleanup(testcase), expected)

    def test_4(self):
        testcase = '(sCeNe1)'
        expected = ''
        self.assertEqual(cleanup(testcase), expected)

    def test_5(self):
        testcase = '(sCeNe10)'
        expected = ''
        self.assertEqual(cleanup(testcase), expected)

    def test_6(self):
        testcase = '(sCeNe    10-13)'
        expected = ''
        self.assertEqual(cleanup(testcase), expected)

    def test_7(self):
        testcase = './ '
        expected = '. '
        self.assertEqual(cleanup(testcase), expected)

    def test_8(self):
        testcase = ' // '
        expected = ' '
        self.assertEqual(cleanup(testcase), expected)


unittest.main()
