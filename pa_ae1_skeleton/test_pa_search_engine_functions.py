import os
import unittest
from pa_search_engine import sanitize_word, parse_line, extract_file_lines, index_file, invert_index_to_file, term_freq_to_file

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

    filepath1 = os.path.join(os.getcwd(), 'pa_ae1_skeleton','test_dir', 'test_file1.txt')
    filepath2 = os.path.join(os.getcwd(), 'pa_ae1_skeleton','test_dir', 'test_file2.txt')
    forward_index = {}
    invert_index = {}
    term_freq = {}
    doc_rank = {}
    individual_word_count = {}
    
    def test_extract_file_lines(self):
        print(extract_file_lines(test_index_file.filepath1))
        print()

    def test_index_file_forward_index(self):
        index_file('test_file1.txt',test_index_file.filepath1, test_index_file.forward_index, test_index_file.invert_index, test_index_file.term_freq, test_index_file.doc_rank)
        #index_file('test_file2.txt',test_index_file.filepath2, test_index_file.forward_index, test_index_file.invert_index, test_index_file.term_freq, test_index_file.doc_rank)
        #print(test_index_file.forward_index)

    def test_invert_index_to_file(self):
        invert_index_to_file('test', test_index_file.filepath1, test_index_file.invert_index)

    def test_freq_to_file(self):
        term_freq_to_file('test', test_index_file.individual_word_count)

        
        


if __name__ == '__main__':
    unittest.main()


