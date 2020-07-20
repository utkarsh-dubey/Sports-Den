# Generated by Django 3.0.7 on 2020-07-20 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='others', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.SlugField(blank=True, editable=False, max_length=100),
        ),
    ]