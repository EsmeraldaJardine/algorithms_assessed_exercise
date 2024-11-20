import os
import unittest
from pa_search_engine import sanitize_word, parse_line, extract_file_lines

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
        line4 = ''
        self.assertEqual(parse_line(line_1), ['hello', 'world'])
        self.assertEqual(parse_line(line_2), ['hello', 'world'])
        self.assertEqual(parse_line(line_3), ['hello', 'world'])
        self.assertEqual(parse_line(line4), [])

class test_index_file(unittest.TestCase):
    def test_extract_file_lines(self):
        filepath = os.path.join(os.getcwd(), 'pa_ae1_skeleton','test_dir', 'test_file.txt')
        print(extract_file_lines(filepath))
        


if __name__ == '__main__':
    unittest.main()


