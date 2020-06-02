from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



class Pictures(models.Model):
    image = models.ImageField(upload_to='images/',default='default.jpg')
    caption = models.TextField()
    pub_date=models.DateTimeField()
    likes_total=models.IntegerField(default=0)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)














