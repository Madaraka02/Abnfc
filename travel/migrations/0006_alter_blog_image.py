# Generated by Django 4.0.3 on 2022-03-31 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_blog_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, upload_to='blogs'),
        ),
    ]
