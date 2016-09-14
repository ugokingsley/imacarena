from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
import os.path
#from django.conf.urls. import *
from bookmarks.views import *
#from django.views.generic.simple import direct_to_template
from django_comments.forms import CommentForm
from django_comments.models import Comment
from bookmarks.feeds import *



feeds = {'recent': RecentBookmarks,
         'user': UserBookmarks
         }


app_name='bookmarks'

#site_media = os.path.join( os.path.dirname(__file__), 'site_media' )

urlpatterns = [
   #browsing
   url(r'^user/(\w+)/$',views.user_page, name='user_page'),
   url(r'^tag/([^\s]+)/$', views.tag_page, name='tag_page'),
   url(r'^tag/$', views.tag_cloud_page, name='tag_cloud_page'),
   url(r'^search/$', views.search_page, name='search_page'),
   # Ajax
   url(r'^ajax/tag/autocomplete/$', views.ajax_tag_autocomplete, name='ajax_tag_autocomplete'),
   url(r'^popular/$', views.popular_page, name='popular_page'),

   # Comments
   url(r'^bookmark/(\d+)/$', views.bookmark_page, name='bookmark_page'),
   #url(r'^comments/', include('django.comments.urls')),
   #session management
   #url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
   url(r'^logout/$',views.logout_page, name='logout'),
   url(r'^register/$', views.register, name='register'),
   url(r'^login/$', views.user_login, name='login'),

   #account management
   url(r'^save/$', views.bookmark_save_page, name='bookmark_save'),
   url(r'^vote/$', views.bookmark_vote_page, name='bookmark_vote_page'),

   # Friends
   url(r'^friends/(\w+)/$', views.friends_page, name='friends_page'),
   url(r'^friend/add/$', views.friend_add, name='friend_page'),
   url(r'^friend/invite/$', views.friend_invite, name='friend_invite'),
   url (r'^friend/accept/(\w+)/$', views.friend_accept, name="friend_accept"),
   #url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',    { 'document_root': site_media }),
   #url(r'^register/$',views.register_page, name='register_page'),
   #url(r'^register/success/$', direct_to_template,  { 'template_name': 'registration/register_success.html' }),
   #url(r'^register/success/$', direct_to_template,  { 'template': 'registration/register_success.html' }),


   # Feeds
   url(r'^feeds/$', RecentBookmarks(), {'feed_dict': feeds}),
   #url(r'^feeds/user/$', UserBookmarks()),
   #url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',{'feed_dict': feeds}),


]
