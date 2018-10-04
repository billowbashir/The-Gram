from django.db import models


class Comment(models.Model):
    comment=models.CharField(max_length=60)


class Image(models.Model):
    image=models.ImageField(upload_to='photos/')
    caption=models.CharField(max_length=60)
    likes=models.IntegerField()
    post_date = models.DateTimeField(auto_now_add=True)
    comments=models.ForeignKey('Comment')

    class Meta:
        ordering=['post_date']
