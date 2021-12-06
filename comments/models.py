from django.db import models
from django.contrib.auth.models import User
from posts.models import Posts
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank= True)
    post= models.ForeignKey(Posts, on_delete= models.CASCADE, null= True, blank= True)
    comment= models.TextField()

    created_at= models.DateTimeField(default=timezone.now)
    updated_at= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.post)

    def total_comments(self):
        return self.comment.count()
