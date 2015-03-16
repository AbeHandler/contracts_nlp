from contract_parser import tokenize
from contract_parser import can_convert_to_float
from contract_parser import get_number_words
from contract_parser import has_dollar_sign

import unittest



class TestTokenizing(unittest.TestCase) :

    def test_split_on_punc(self) :

        assert tokenize('foo,bar') == ['foo,', 'bar']
    

    def test_can_convert_to_float(self):
        assert can_convert_to_float("$23403")

    def test_can_not_convert_to_float(self):
        assert not can_convert_to_float("$2a403")

    def test_has_dollar_sign(self):
        assert has_dollar_sign("$182,000.00")

    def test_spaces(self) :

        assert tokenize('foo bar') == ['foo', 'bar']
        assert tokenize('foo  bar') == ['foo', 'bar']
        assert tokenize('foo bar ') == ['foo', 'bar']
        assert tokenize(' foo bar') == ['foo', 'bar']

if __name__ == '__main__' :
    unittest.main()    
