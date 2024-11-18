import unittest
from pa_search_engine import sanitize_word, parse_line

class test_sanitize_word(unittest.TestCase):
    def test_sanitize_word(self):
        self.assertEqual(sanitize_word('hello'), 'hello')
        self.assertEqual(sanitize_word('HELLO'), 'hello')
        self.assertEqual(sanitize_word('hello!'), 'hello')
        self.assertEqual(sanitize_word('hello,'), 'hello')
    
class test_parse_line(unittest.TestCase):
    def test_parse_line(self):
        line_1 = 'hello world'
        line_2 = 'HELLO WORLD'
        line_3 = '   hello,    world   '
        self.assertEqual(parse_line(line_1), ['hello', 'world'])
        self.assertEqual(parse_line(line_2), ['hello', 'world'])
        self.assertEqual(parse_line(line_3), ['hello', 'world'])


if __name__ == '__main__':
    unittest.main()


