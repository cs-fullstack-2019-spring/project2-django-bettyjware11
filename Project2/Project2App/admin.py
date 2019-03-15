from django.contrib import admin
from .models import WikiPostsModel, RelatedModel, UserModel


# Register your models here.
admin.site.register(WikiPostsModel)
admin.site.register(RelatedModel)
admin.site.register(UserModel)