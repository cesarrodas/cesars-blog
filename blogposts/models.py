from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    username = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    message = models.TextField()
    post_id = models.IntegerField()

    @classmethod
    def create(cls, username, message, post_id):
        comment = cls(username=username, message=message, \
        post_id=post_id, pub_date=timezone.datetime.now())
        return comment

    def __str__(self):
        return self.message[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
