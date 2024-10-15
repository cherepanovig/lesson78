from django.contrib import admin
from .models import Post
from .models import Publisher
from .models import Author

admin.site.register(Post)
admin.site.register(Publisher)
admin.site.register(Author)