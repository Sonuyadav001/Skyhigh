# models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  # Import CKEditor field
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100, default="Untitled Post")  # Default title
    content = RichTextUploadingField()
    
    date_posted = models.DateTimeField(default=timezone.now)  # Post creation time
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Author
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name="posts", null=True, blank=True
    )  # Category
    tags = models.ManyToManyField('Tag', related_name="posts", blank=True)  # Tags

    hero_image = models.ImageField(
        upload_to='blog_images/', null=True, blank=True
    )  # Field for hero image, optional

    def __str__(self):
        return self.title

    def get_hero_image(self):
        """
        Returns the hero image URL if available; otherwise, returns the default image URL.
        """
        if self.hero_image and hasattr(self.hero_image, 'url'):
            return self.hero_image.url
        return "/media/blog_images/default.png"  # Ensure this path exists in your media folder



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"
