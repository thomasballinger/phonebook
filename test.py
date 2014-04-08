import main
import unittest

class TestParser(unittest.TestCase):

    def test_shuffle(self):
        args = main.parse_args(['add', 'tom', '123-456-7890', '-b', 'phonebook'])
        self.assertEqual(vars(args), {'func':main.add, 'name':'tom', 'phonebook':['phonebook'], 'number':'123-456-7890'})

if __name__ == '__main__':
    unittest.main()
