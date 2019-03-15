# Generated by Django 2.0.6 on 2019-03-15 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemTitle', models.CharField(default='', max_length=200)),
                ('itemText', models.CharField(default='', max_length=2000)),
                ('createdDateTime', models.DateField(default=django.utils.timezone.now)),
                ('lastUpdatedDateTime', models.DateField(default=django.utils.timezone.now)),
                ('optionalPostImage', models.CharField(default='', max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=200)),
                ('password1', models.CharField(default='', max_length=200)),
                ('password2', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WikiPostsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postTitle', models.CharField(default='', max_length=200)),
                ('postText', models.TextField(max_length=5000)),
                ('createdDateTime', models.DateField(default=django.utils.timezone.now)),
                ('lastUpdatedDateTime', models.DateField(default=django.utils.timezone.now)),
                ('optionalPostImage', models.CharField(default='', max_length=800)),
                ('foreignkeyToUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='relatedmodel',
            name='foreignKeyToWikiPost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project2App.WikiPostsModel'),
        ),
    ]
