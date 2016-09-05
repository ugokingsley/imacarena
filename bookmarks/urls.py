from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
import os.path
#from django.conf.urls. import *
from bookmarks.views import *

app_name='bookmarks'

#site_media = os.path.join( os.path.dirname(__file__), 'site_media' )

urlpatterns = [
   url(r'^user/(\w+)/$',views.user_page, name='user_page'),
   #url(r'^(\w+)/$',views.user_page, name='user_page'),
   url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
   url(r'^logout/$', auth_views.logout, name='logout'),
   #url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',    { 'document_root': site_media }),
]