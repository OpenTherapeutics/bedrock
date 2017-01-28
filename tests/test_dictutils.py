import pytest
from bedrock import dictutils

class TestDictUtils:

    def test_overlay(self):

        DEFAULT_CONFIG = {
            'foo': 'bar',
            'spam': {
                'eggs': 'sausage and spam',
                'bacon': 'spam spam eggs and spam'
            },
            'birds': {
                'parrots': {
                    'alive': 0,
                    'dead': ['demised', 'kicked the bucket', 'is no more'],
                },
                'swallows': {
                    'african': 'migratory',
                    'european': 42
                }
            }
        }

        partial = {
            'birds': { 'parrots': {'alive': 1}, 'swallows' : {'european': -1}},
            'foo': 'baz',
            'spanish inquisition': 'nobody expects'
        }

        result = dictutils.overlay(DEFAULT_CONFIG, partial)
        assert result == {
            'birds': {
                'parrots': {
                    'alive': 1,
                    'dead': ['demised', 'kicked the bucket', 'is no more']
                },
                'swallows': {'african': 'migratory', 'european': -1}},
                'foo': 'baz',
                'spam': {
                    'bacon': 'spam spam eggs and spam',
                    'eggs': 'sausage and spam'
                },
                'spanish inquisition': 'nobody expects'
            }
