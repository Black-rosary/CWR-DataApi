# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.interested_party import PublisherForWriterRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Publisher For Writer (PWR) records grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

_factory_field = DefaultFieldFactory(_config.load_field_config('common'))

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

"""
Patterns.
"""

publisher = _factory_record.get_transaction_record('writer_publisher')

"""
Parsing actions for the patterns.
"""

publisher.setParseAction(lambda p: _to_publisher(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_publisher(parsed):
    """
    Transforms the final parsing result into a WriterPublisherRecord instance.

    :param parsed: result of parsing a Writer Publisher record
    :return: a WriterPublisherRecord created from the parsed record
    """
    return PublisherForWriterRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                    parsed.publisher_ip_n, parsed.writer_ip_n, parsed.submitter_agreement_n,
                                    parsed.society_assigned_agreement_n)