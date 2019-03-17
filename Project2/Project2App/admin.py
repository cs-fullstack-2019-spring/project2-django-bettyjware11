from django.contrib import admin
from .models import WikiPostsModel, RelatedModel, AuthorModel


# Register your models here.
admin.site.register(WikiPostsModel)
admin.site.register(RelatedModel)
admin.site.register(AuthorModel)