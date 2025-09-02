from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=50, null=False, blank=False)
    blog_img = models.ImageField(upload_to='uploads/', blank=True, null=True)
    blog_text = models.TextField(blank=False, null= False)
    blog_upload = models.DateTimeField(default=timezone.now())
    blog_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.blog_title}"


class BlogReview(models.Model):
    RATING_CHOICE = [
        (1, "Bad"),
        (2, "Normal"),
        (3, "Good"),
        (4, "Very Good"),
        (5, "Excellent")
    ]
    r_blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='reviews') # this create a relation
    rating = models.IntegerField(max_length=1, choices=RATING_CHOICE)
    reviewer_name = models.CharField(max_length=30)
    comment = models.CharField(blank=True)
    r_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.r_blog.user} - {self.comment}"