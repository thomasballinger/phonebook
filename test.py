import main
import argparse
import unittest

class TestParser(unittest.TestCase):

    def test_parse_add(self):
        args = main.parse_args(['add', 'tom', '123-456-7890', '-b', 'phonebook'])
        self.assertEqual(vars(args), {'func':main.add, 'name':'tom', 'phonebook':['phonebook'], 'number':'123-456-7890'})
        self.assertRaises(argparse.ArgumentError, main.parse_args, ['add', 'tom', '123123-456-7890', '-b', 'phonebook'])

class TestPhonebook(unittest.TestCase):
    def test_create(self):
        1#main.Phonebook()


if __name__ == '__main__':
    unittest.main()
