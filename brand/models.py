from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(
        upload_to='brand_logos/',
        null=True,
        blank=True,
        default='brand_images/default.png'  # Same default image as hero_image
    )
    slogan = models.CharField(max_length=255, blank=True)
    content = RichTextUploadingField()
    hero_image = models.ImageField(
        upload_to='brand_images/',
        null=True,
        blank=True,
        default='brand_images/default.png'  # Default image
    )

    def __str__(self):
        return self.name


class BrandGallery(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='brand_gallery/')

    def __str__(self):
        return f"Gallery Image for {self.brand.name}"
