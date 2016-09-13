from django.contrib import admin
from models import Link,Bookmark,UserProfile,Tag,SharedBookmark
# Register your models here.

admin.site.register(Link)
admin.site.register(Bookmark)
admin.site.register(UserProfile)
admin.site.register(Tag)
admin.site.register(SharedBookmark)