from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_info = models.TextField()
    picture = models.ImageField(upload_to='post/', blank=True,default='')
    name = models.CharField(max_length=50)

    def save_profile(self):
        self.save

    def delete_user(self):
        self.delete()

    
    @classmethod
    def edit_profile(cls, id, value):
        cls.objects.filter(id=id).update(profile_name=value)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    image = models.ImageField(upload_to='post/', blank=True ,default = 'default.jpg')
    title = models.CharField(max_length=30, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    caption = models.TextField(max_length=300)

    @classmethod
    def all_posts(cls) :
        posts = cls.objects.all()
        return posts

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def update_post(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    
class Comment(models.Model):
    comment_content = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def save_comment(self):
        self.save()


class Like(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    control = models.CharField(max_length=50,unique=True, null=True)

    def __str__(self):
        return self.control

    def save_like(self):
        self.save()


class Follow(models.Model):
    username = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    follow_id = models.CharField(max_length=50,unique=True, null=True)

    def __str__(self):
        return self.follow_id

    def save_like(self):
        self.save()