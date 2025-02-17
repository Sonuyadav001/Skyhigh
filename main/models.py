from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# Signal to notify admin of new subscriptions
@receiver(post_save, sender=NewsletterSubscription)
def notify_admin_on_subscription(sender, instance, created, **kwargs):
    if created:
        # Customize the admin email address
        admin_email = settings.ADMINS[0][1] if settings.ADMINS else None
        if admin_email:
            send_mail(
                subject="New Newsletter Subscription",
                message=f"A new user has subscribed to the newsletter: {instance.email}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[admin_email],
                fail_silently=True,
            )

from django.db import models

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Add this field

    def __str__(self):
        return f"Message from {self.first_name} ({self.email})"



class FAQ(models.Model):
    question = models.CharField(max_length=255, unique=True)  # Ensure unique questions
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Store creation time
    updated_at = models.DateTimeField(auto_now=True)  # Track updates

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-created_at']  # Show latest FAQs first


class Privacy(models.Model):
    privacy = models.CharField(max_length=255, unique=True)  # Ensure unique questions
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Store creation time
    updated_at = models.DateTimeField(auto_now=True)  # Track updates

    def __str__(self):
        return self.privacy

    class Meta:
        ordering = ['-created_at']  


class Term(models.Model):
    term = models.CharField(max_length=255, unique=True)  # Ensure unique questions
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Store creation time
    updated_at = models.DateTimeField(auto_now=True)  # Track updates

    def __str__(self):
        return self.term

    class Meta:
        ordering = ['-created_at']  






class Service(models.Model):
    title = models.CharField(max_length=100, default="Untitled Service")
    description = models.TextField()
    content = RichTextUploadingField()
    hero_image = models.ImageField(
        upload_to='service_images/',
        null=True,
        blank=True,
        default='service_images/default.png'  # Ensure this file exists in your media directory
    )

    def __str__(self):
        return self.title



class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="sub_services")
    title = models.CharField(max_length=100)
    description = RichTextUploadingField()  # Updated to RichTextUploadingField

    def __str__(self):
        return f"{self.title} - {self.service.title}"



class SubServiceImage(models.Model):
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='subservice_images/', default='subservice_images/default_image.jpg')

    def __str__(self):
        return f"Image for {self.sub_service.title}"


from django.db import models

class Brochure(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='brochures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
