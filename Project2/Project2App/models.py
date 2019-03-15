from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=200, default="")
    password1 = models.CharField(max_length=200, default='')
    password2 = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=256, unique=True)

    def __str__(self):
        return self.username



class WikiPostsModel(models.Model):
    postTitle= models.CharField(max_length=200, default="")
    postText= models.TextField(max_length=5000)
    createdDateTime= models.DateField(default= timezone.now)
    lastUpdatedDateTime= models.DateField(default= timezone.now)
    optionalPostImage= models.CharField(max_length=800, default="")
    # optionalPostImage= models.ImageField(upload_to='entries')
    foreignkeyToUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.postTitle


class RelatedModel(models.Model):
    itemTitle = models.CharField(max_length=200, default="")
    itemText = models.TextField(max_length=5000)
    createdDateTime = models.DateField(default= timezone.now)
    lastUpdatedDateTime= models.DateField(default= timezone.now)
    optionalPostImage= models.CharField(max_length=800, default="")
    # optionalPostImage= models.ImageField(upload_to='relateds')
    foreignKeyToWikiPost = models.ForeignKey(WikiPostsModel, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.itemTitle


