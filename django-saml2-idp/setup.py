from setuptools import setup, find_packages
import saml2idp

classifiers = []
install_requires = open('requirements.txt', 'rb').read().strip().split()

setup(
    name                    = 'django-saml2-idp',
    long_description        = 'SAML 2.0 Identity Provider app for Django projects.',
    version                 = saml2idp.__version__,
    author                  = saml2idp.__author__,
    author_email            = saml2idp.__author_email__,
    description             = saml2idp.__description__,
    license                 = saml2idp.__license__,
    url                     = saml2idp.__homepage__,
    install_requires        = install_requires,
    packages                = find_packages(),
    include_package_data    = True,
    classifiers             = classifiers
)
