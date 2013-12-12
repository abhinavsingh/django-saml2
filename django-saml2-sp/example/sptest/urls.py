from django.conf.urls.defaults import *
from django.contrib.auth.views import logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

try:
    from django.conf import settings
    logout_url = settings.LOGOUT_URL
    if logout_url[0] == '/':
        logout_url = logout_url[1:]
except:
    logout_url = 'accounts/logout/'

urlpatterns = patterns('',
    url(r'^' + logout_url, logout, name='logout_url'),
    (r'^admin/', include(admin.site.urls)),
    (r'^sp/', include('saml2sp.urls')),
)
