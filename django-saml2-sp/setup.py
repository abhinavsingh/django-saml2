from setuptools import setup, find_packages
import saml2sp

classifiers = []
install_requires = open('requirements.txt', 'rb').read().strip().split()

setup(
    name                    = 'django-saml2-sp',
    long_description        = 'SAML 2.0 Service Provider app for Django projects.',
    version                 = saml2sp.__version__,
    author                  = saml2sp.__author__,
    author_email            = saml2sp.__author_email__,
    description             = saml2sp.__description__,
    license                 = saml2sp.__license__,
    url                     = saml2sp.__homepage__,
    install_requires        = install_requires,
    packages                = find_packages(),
    include_package_data    = True,
    classifiers             = classifiers
)
