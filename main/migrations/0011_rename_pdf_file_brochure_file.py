# Generated by Django 5.1.3 on 2025-02-04 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_brochure'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brochure',
            old_name='pdf_file',
            new_name='file',
        ),
    ]
