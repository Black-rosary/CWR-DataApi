# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Message grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestMessageGrammar(unittest.TestCase):
    """
    Tests that the Message grammar decodes correctly formatted strings
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_transaction_record('message')

    def test_valid_full(self):
        """
        Tests that NWN grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'MSG0000123400000023F00001235AGRE123MESSAGE                                                                                                                                               '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('MSG', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('F', result.message_type)
        self.assertEqual(1235, result.original_record_sequence_n)
        self.assertEqual('AGR', result.message_record_type)
        self.assertEqual('E', result.message_level)
        self.assertEqual(123, result.validation_n)
        self.assertEqual('MESSAGE', result.message_text)