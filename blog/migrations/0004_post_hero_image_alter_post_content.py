# Generated by Django 5.1.3 on 2025-01-07 02:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_tag_post_category_comment_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hero_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(default='This is a default content.'),
        ),
    ]
