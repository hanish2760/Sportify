from django.db import models
from django.contrib.auth.models import User


class Sport(models.Model):
    sport_title = models.CharField(max_length=50)
    sport_image=models.ImageField(upload_to='sports_images/', null=True, blank=True)
    def __str__(self):
        return self.sport_title
    #image


class Location(models.Model):
    loc = models.CharField(max_length=50)

    def __str__(self):
        return self.loc

class Ground(models.Model):
    ground_name=models.CharField(max_length=50)
    ground_image = models.ImageField(upload_to='grounds_images/', null=True, blank=True)
    ground_loc=models.ForeignKey(Location,on_delete=models.CASCADE)
    def __str__(self):
        return self.ground_name

class UserProfile(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    sports=models.ManyToManyField(Sport,blank=True)
    grounds=models.ManyToManyField(Ground,blank=True)
    verified=models.BooleanField(default=False)
    # if  2 users uploads images with same file name then ??
    display_picture= models.ImageField(upload_to='profile_images/', null=True, blank=True)
    location=models.ManyToManyField(Location,blank=True)

    def __str__(self):
        return self.user

# class Notification(models.Model):
#     notification_msg=models.CharField(max_length=250)
#     viewed=models.BooleanField(default=False)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
# Notiiaction is business logic??
# Create your models here.

#using taggit to apply tags!
#list all posts tagged with a specific tag
# from taggit.managers import TaggableManager
#
# class SportsTags(models.Model):
#     tags=TaggableManager()
# class GroundTags(models.Model):
#     tags=TaggableManager()
# class UserTags(models.Model):
#     tags=TaggableManager()

 # sports_tags=models.OneToOneField(
    #     SportsTags,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
    # ground_tags = models.OneToOneField(
    #     GroundTags,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
    # user_tags = models.OneToOneField(
    #     UserTags,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
    #post.tags.add('music', 'jazz', 'django')

class Post(models.Model):
    post_message=models.TextField(blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    # slug = models.SlugField(max_length=250,
    #                         unique_for_date='publish')
    #edit admin.py to register this to amdin site admin.site.register(Post)
    # check out what slug can be useful for like searching off posts as it maekes a url for each post
    post_image=models.ImageField(upload_to='uploaded_media', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ground=models.OneToOneField
    match_dateTime=models.CharField(max_length=150,null=True)

    #likes
    #Add user  activity refer the ddjango by example book!
    def __str__(self):
        return self.user

# to search for posts case insensitive
#can add notifications later.
#Post.objects.filter(body__icontains='framework')





class Comment(models.Model):
    comment_message = models.TextField(blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

