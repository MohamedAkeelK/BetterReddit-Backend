# Generated by Django 4.1.3 on 2022-11-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breddit', '0019_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='avatars'),
        ),
    ]