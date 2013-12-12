"""
XML string templates for SAML 2.0 Service Provider AuthnRequest.

NOTE #1: OK, encoding XML into python is not optimal.
    However, this is the easiest way to get canonical XML...
    ...at least, without requiring other XML-munging libraries.
    I'm not including the indentation in the XML itself, because that messes
    with its canonicalization. This is meant to produce one long one-liner.
    I am indenting each line in python, for my own happiness. :)

NOTE #2: I'm using string.Template, rather than Django Templates, to avoid
    the overhead of loading Django's template code. (KISS, baby.)
"""
#XXX: SIGNED_INFO and SIGNATURE are identical to those used in saml2idp.
# Someday, it might be good to move the signing stuff into a common module
# that is shared by both libraries. YAGNI?
SIGNED_INFO = (
    '<ds:SignedInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">'
        '<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"></ds:CanonicalizationMethod>'
        '<ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"></ds:SignatureMethod>'
        '<ds:Reference URI="#${REFERENCE_URI}">'
            '<ds:Transforms>'
                '<ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"></ds:Transform>'
                '<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"></ds:Transform>'
            '</ds:Transforms>'
            '<ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"></ds:DigestMethod>'
            '<ds:DigestValue>${SUBJECT_DIGEST}</ds:DigestValue>'
        '</ds:Reference>'
    '</ds:SignedInfo>'
)
SIGNATURE = (
    '<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">'
        '${SIGNED_INFO}'
    '<ds:SignatureValue>${RSA_SIGNATURE}</ds:SignatureValue>'
    '<ds:KeyInfo>'
        '<ds:X509Data>'
            '<ds:X509Certificate>${CERTIFICATE}</ds:X509Certificate>'
        '</ds:X509Data>'
    '</ds:KeyInfo>'
'</ds:Signature>'
)

AUTHN_REQUEST = (
    '<?xml version="1.0" encoding="UTF-8"?>'
        '<samlp:AuthnRequest AssertionConsumerServiceURL="${ACS_URL}" '
                'Destination="${DESTINATION}" '
                'ID="${AUTHN_REQUEST_ID}" '
                'IssueInstant="${ISSUE_INSTANT}" '
                'ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" '
                'Version="2.0" '
                'xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol">'
            '<saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">${ISSUER}</saml:Issuer>'
            # I THINK THIS...
            '${AUTHN_REQUEST_SIGNATURE}'
            # ...REPLACES THIS:
#            '<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">'
#                '<ds:SignedInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">'
#                    '<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" xmlns:ds="http://www.w3.org/2000/09/xmldsig#"/>'
#                    '<ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" xmlns:ds="http://www.w3.org/2000/09/xmldsig#"/>'
#                    '<ds:Reference URI="${REFERENCE_URI}" xmlns:ds="http://www.w3.org/2000/09/xmldsig#">'
#                        '<ds:Transforms xmlns:ds="http://www.w3.org/2000/09/xmldsig#">'
#                            '<ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" xmlns:ds="http://www.w3.org/2000/09/xmldsig#"/>'
#                            '<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ec:InclusiveNamespaces PrefixList="ds saml samlp" xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#"/></ds:Transform>'
#                        '</ds:Transforms>'
#                        '<ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" xmlns:ds="http://www.w3.org/2000/09/xmldsig#"/>'
#                        '<ds:DigestValue xmlns:ds="http://www.w3.org/2000/09/xmldsig#">UwnBYwYd4wkS0Ox5/4s5QwQ7RCU=</ds:DigestValue>'
#                    '</ds:Reference>'
#                '</ds:SignedInfo>'
#            '<ds:SignatureValue xmlns:ds="http://www.w3.org/2000/09/xmldsig#">'
#                '${SIGNATURE_VALUE}'
#            '</ds:SignatureValue>'
#            '<ds:KeyInfo>'
#                '<ds:X509Data>'
#                    '<ds:X509Certificate>'
#                    '${CERTIFICATE}'
#                    '</ds:X509Certificate>'
#                '</ds:X509Data>'
#            '</ds:KeyInfo>'
#        '</ds:Signature>'
    '</samlp:AuthnRequest>'
)
