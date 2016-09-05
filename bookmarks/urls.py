from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name='bookmarks'
urlpatterns = [
   url(r'^user/(\w+)/$',views.user_page, name='user_page'),
   #url(r'^(\w+)/$',views.user_page, name='user_page'),
   url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
]