# Generated by Django 4.0.3 on 2022-04-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ig', '0002_rename_user_profile_username_post_likes_like_follow_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='', upload_to='profile/'),
        ),
    ]