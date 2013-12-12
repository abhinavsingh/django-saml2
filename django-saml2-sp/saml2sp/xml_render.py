"""
Functions for creating XML output.
"""
import logging
import string
from xml_signing import get_signature_xml
from xml_templates import AUTHN_REQUEST

def _get_authnrequest_xml(template, parameters, signed=False):
    # Reset signature.
    params = {}
    params.update(parameters)
    params['AUTHN_REQUEST_SIGNATURE'] = ''
    template = string.Template(template)

    unsigned = template.substitute(params)
    logging.debug('Unsigned:')
    logging.debug(unsigned)
    if not signed:
        return unsigned

    # Sign it.
    signature_xml = get_signature_xml(unsigned, params['AUTHN_REQUEST_ID'])
    params['AUTHN_REQUEST_SIGNATURE'] = signature_xml
    signed = template.substitute(params)

    logging.debug('Signed:')
    logging.debug(signed)
    return signed

def get_authnrequest_xml(parameters, signed=False):
    return _get_authnrequest_xml(AUTHN_REQUEST, parameters, signed)
