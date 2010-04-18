from django.conf.urls.defaults import *
from ecomstore import settings

from django.contrib import admin
admin.autodiscover()

import os
static = os.path.join(
                      os.path.dirname(__file__), 'static'
)

urlpatterns = patterns('',
                       (r'^catalog/?', 'preview.views.home'),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^', include('catalog.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
          { 'document_root' : static }),
)

handler404 = 'ecomstore.views.file_not_found_404'