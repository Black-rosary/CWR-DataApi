# -*- coding: utf-8 -*-

from abc import ABCMeta
import logging

import pyparsing as pp

from cwr.grammar.field import record as field_record


"""
Record fields factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

"""
Configuration classes.
"""


class PrefixBuilder(object):
    def __init__(self, config):
        self._config = config

    def get_prefix(self, id):
        return field_record.record_prefix(self._config[id])


class RecordFactory(object):
    """
    Factory for acquiring record rules.
    """
    __metaclass__ = ABCMeta

    _lineStart = pp.lineStart.suppress()
    _lineStart.setName("Start of line")

    _lineEnd = pp.lineEnd.suppress()
    _lineEnd.setName("End of line")

    def __init__(self, record_configs, prefixer, field_factory):
        # records already created
        self._records = {}
        # Logger
        self._logger = logging.getLogger(__name__)
        # Configuration for creating the record
        self._record_configs = record_configs
        # Fields factory
        self._field_factory = field_factory
        # Prefix builder
        self._prefixer = prefixer

    def get_record(self, id):
        record = self._lineStart + \
                 self._prefixer.get_prefix(id) + \
                 self._build_record(id) + \
                 self._lineEnd

        return record

    def _build_record(self, id):
        field_config = self._record_configs[id]

        fields = []
        for config in field_config:
            if 'compulsory' in field_config:
                compulsory = field_config['compulsory']
            else:
                compulsory = False

            fields.append(self._field_factory.get_field(config['name'], compulsory=compulsory))

        if len(fields) > 0:
            first = True
            record = None
            for field in fields:
                if first:
                    record = field
                    first = False
                else:
                    record += field
        else:
            record = None

        return record