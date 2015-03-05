# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar.record import nra_record


"""
CWR Non-Roman Alphabet Publisher Name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNPNGrammar(unittest.TestCase):
    """
    Tests that the NPN grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = nra_record.npn

    def test_valid_full(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NPN000012340000002312A12345678THE NAME                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ES'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPN', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual(12, result.sequence_n)
        self.assertEqual('A12345678', result.ip_id)
        self.assertEqual('THE NAME', result.name)
        self.assertEqual('ES', result.language)