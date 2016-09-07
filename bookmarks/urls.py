from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
import os.path
#from django.conf.urls. import *
from bookmarks.views import *
#from django.views.generic.simple import direct_to_template


app_name='bookmarks'

#site_media = os.path.join( os.path.dirname(__file__), 'site_media' )

urlpatterns = [
   #browsing
   url(r'^user/(\w+)/$',views.user_page, name='user_page'),

   #session management
   url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
   url(r'^logout/$',views.logout_page, name='logout'),
   url(r'^register/$', views.register, name='register'),

   #account management
   url(r'^save/$', views.bookmark_save_page, name='bookmark_save'),
   #url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',    { 'document_root': site_media }),
   #url(r'^register/$',views.register_page, name='register_page'),
   #url(r'^register/success/$', direct_to_template,  { 'template_name': 'registration/register_success.html' }),
   #url(r'^register/success/$', direct_to_template,  { 'template': 'registration/register_success.html' }),
]
