import unittest
from tokenizer import Token, Tokenizer

class TokenizerTest(unittest.TestCase):
    '''tests for tokenizer.py'''
    
    def test_regular(self):
        '''
        tests a string with mixed alphabetical symbols, numbers, and whitespaces
        '''
        tokens = Tokenizer.tokenize('jhg ghj 467 fgh')
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].pos, 0)
        self.assertEqual(tokens[0].word, 'jhg')
        self.assertEqual(tokens[1].pos, 4)
        self.assertEqual(tokens[1].word, 'ghj')
        
    def test_typeError(self):
        '''
        tests how the tokenizer handles receiving an integer instead of a string
        as input
        '''
        with self.assertRaises(TypeError):
            Tokenizer.tokenize(123)
            
    def test_whitespaces(self):
        '''
        tests a string that starts and ends with a whitespace and has multiple
        whitespaces in a row
        '''
        tokens = Tokenizer.tokenize('  jhg  jhf  kjg  ')
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].pos, 2)
        self.assertEqual(tokens[0].word, 'jhg')
        self.assertEqual(tokens[2].pos, 12)
        self.assertEqual(tokens[2].word, 'kjg')       
        
    def test_punctiation(self):
        '''
        tests a string with several puctuation marks
        '''
        tokens = Tokenizer.tokenize('two,:;!words/.')
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[1].pos, 7)
        self.assertEqual(tokens[1].word, 'words')
        
    def test_noLetters(self):
        '''
        tests a string that contains no alphabetical symbols
        '''
        tokens = Tokenizer.tokenize(' 678 /// .;!57')
        self.assertEqual(len(tokens), 0)
        
    
if __name__ == '__main__':
    unittest.main()
