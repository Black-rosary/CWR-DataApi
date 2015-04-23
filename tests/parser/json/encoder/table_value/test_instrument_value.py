# -*- coding: utf-8 -*-

import unittest
import json

from cwr.parser.cwrjson import JSONEncoder
from cwr.table_value import InstrumentValue


"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestInstrumentValueEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = InstrumentValue('BBF', 'Bamboo Flute', 'National/Folk', 'same as Dizi or D\'Tzu')

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual('BBF', encoded['code'])
        self.assertEqual('Bamboo Flute', encoded['name'])
        self.assertEqual('National/Folk', encoded['family'])
        self.assertEqual('same as Dizi or D\'Tzu', encoded['description'])