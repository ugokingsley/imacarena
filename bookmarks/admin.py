from django.contrib import admin
from models import Link,Bookmark,UserProfile,Tag,SharedBookmark,Friendship
from django_comments.models import Comment
# Register your models here.

admin.site.register(Link)
admin.site.register(Bookmark)
admin.site.register(UserProfile)
admin.site.register(Tag)
admin.site.register(SharedBookmark)
admin.site.register(Comment)
admin.site.register(Friendship)