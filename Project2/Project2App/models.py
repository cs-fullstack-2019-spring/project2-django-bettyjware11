from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class AuthorModel(models.Model):
    username = models.CharField(max_length=200, default="")
    password1 = models.CharField(max_length=200, default='')
    password2 = models.CharField(max_length=200, default='')
    foreignkeyToUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "The author is: " + str(self.username)


class WikiPostsModel(models.Model):
    postTitle= models.CharField(max_length=200, default="")
    postText= models.TextField(max_length=5000)
    createdDateTime= models.DateTimeField(auto_now_add=True)
    lastUpdatedDateTime= models.DateTimeField(auto_now=True)
    optionalPostImage= models.ImageField(blank=True, null=True, upload_to="images/%Y/%m/%d/")
    foreignkeyToAuthor = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return "The Wiki Post is" + str(self.postTitle)


class RelatedModel(models.Model):
    itemTitle = models.CharField(max_length=200, default="")
    itemText = models.TextField(max_length=5000)
    createdDateTime = models.DateTimeField(auto_now_add=True)
    lastUpdatedDateTime= models.DateTimeField(auto_now=True)
    optionalPostImage= models.ImageField(blank=True, null=True, upload_to="images/%Y/%m/%d/")
    foreignKeyToWikiPosts = models.ForeignKey(WikiPostsModel, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return "The related article is" + self.itemTitle


