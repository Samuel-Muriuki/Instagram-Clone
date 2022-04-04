from django.test import TestCase
from .models import Profile,Post,Comment
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.Samm = Profile(name = 'Samm', profile_pic = 'image.jpg', bio='Engineers at instagram')
        self.Samm.save()

    def tearDown(self):
        Profile.objects.all().delete()
    

    def test_instance(self):
        self.assertTrue(isinstance(self.Samm, Profile))

    def test_save_method(self):
        self.Samm.save_profile()
        name = Profile.objects.all()

    
class PostTestCase(TestCase):

    def setUp(self):
        self.engineering = Profile(image= 'image.jpg', title = 'engineering', user='User')
        self.engineering.save()


    def tearDown(self):
        Post.objects.all().delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.engineering, Post))


    def  test_save_method(self):
        self.Samm.save_post()
        tittle = Post.objects.all()



class CommentTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='thomas',password='nstgrmtoto29')
        self.comment = Comment(comment='Test Comment',username=self.new_user,post=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def tearDown(self):
        Comment.objects.all().delete()

    def test_save_method(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)

    
