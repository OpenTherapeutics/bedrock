from __future__ import unicode_literals
import pytest
import re
from bedrock import strutils

class TestReplaceString:
    '''
    Tests for ``replace`` using strings.
    
    Signature: ::
    
        replace(text, old, new, count=None, strip=False)
        
    '''
    # 
    
    def test_replace_1(self):
        assert ('is expected' == strutils.replace(
            '  not expected \t \n',
            'not',
            'is',
            strip=True
        ))


class TestReplaceRegex:
    '''
    Tests for ``replace`` using regular expression.
    
    Signature: ::
    
        replace(text, old, new, count=None, strip=False)
        
    '''
    
    def test_replace_re1(self):
        assert ('here are random numbers' == strutils.replace(
            'here are 123 random 456 numbers',
            re.compile(r'\s+\d+\s+'),
            ' '
        ))


class TestSplitter:
    '''
    Signature: ::
    
        def splitter(text, token=None, expected=2, default='', strip=False)
        
    '''
    def test_splitter_1(self):
        assert (['Hello, world', '', '', ''] == strutils.splitter(
            'Hello, world',
            token='@',
            expected=4
        ))

    def test_splitter_2(self):
        assert (['Hello,', 'world', ''] == strutils.splitter('Hello, world', expected=3))
        
    def test_splitter_3(self):
        assert (['1', '2', '0'] == strutils.splitter(
            'X 1 Y 2',
            re.compile(r' ?[A-Z] ?'),
            expected=3,
            default='0'
        ))
    
class TestReplaceEach:
    
    def test_replace_each_1(self):
        assert (
            strutils.replace_each(
                'line 1\nline 2\nline 3',
                (('line', 'Line'), (re.compile(r'(\d+)'), r'#\1'))
            ) == 'Line #1\nLine #2\nLine #3'
        )


