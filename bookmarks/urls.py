from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^(\w+)/$',views.user_page, name='user_page'),
]