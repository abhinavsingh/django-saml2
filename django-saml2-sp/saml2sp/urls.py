from django.conf.urls.defaults import *
from views import (
    descriptor,
    sso_idp_select,
    sso_response,
    sso_single_logout,
    sso_test,
)

urlpatterns = patterns('',
    # Example:
    # (r'^sptest/', include('sptest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    (r'^test/$', sso_test),
    (r'^idpselect/$', sso_idp_select),
    (r'^acs/$', sso_response),
    url(r'^singlelogout/$', sso_single_logout, name='sso_single_logout'),
    url(r'^metadata/', descriptor, name='spssodescriptor'),
)
