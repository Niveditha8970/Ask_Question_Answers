from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Custom User Model #using Abstractuser class we can create custmuser model
class CustomUser(AbstractUser):
    bio=models.TextField()
    location=models.CharField(max_length=200)

# Create your models here.
#Question Model
class Question(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    detail=models.TextField()
    tags=models.TextField(default='')
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title #this is dafult which will show in admin panel

#Answer Model 
class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.detail
    
# comment
class Comment(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='comment_user')
    comment=models.TextField(default='')
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

#likes
class UpVote(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='upvote_user')

#Dislikes
class DownVote(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='downvote_user')