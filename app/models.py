from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Comment(models.Model):
    comment=models.CharField(max_length=60)
class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='profile_photos/')
    bio=models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_profile(self):
        self.save()
    @classmethod
    def search_by_profile(cls,search_term):
        profiles=cls.objects.filter(user__icontains=search_term)
        return profiles

class Image(models.Model):
    image=models.ImageField(upload_to='photos/')
    caption=HTMLField()
    likes=models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    comments=models.ForeignKey('Comment',null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering=['-post_date']

    def save_image (self):
        self.save()

    def delete_image(self):
        self.delete()
    @classmethod
    def update_caption(cls,id,caption):
        new_caption=Image.filter_by(id=id).update(caption=caption)
        return new_caption
