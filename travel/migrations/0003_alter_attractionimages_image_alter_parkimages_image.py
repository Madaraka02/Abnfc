# Generated by Django 4.0.3 on 2022-03-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_alter_attractionimages_image_alter_parkimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractionimages',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='attimagesm'),
        ),
        migrations.AlterField(
            model_name='parkimages',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='parksm'),
        ),
    ]