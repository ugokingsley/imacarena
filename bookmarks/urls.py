from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^(\w+)/$',views.user_page, name='user_page'),
]