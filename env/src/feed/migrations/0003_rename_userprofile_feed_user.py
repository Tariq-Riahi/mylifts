# Generated by Django 4.1.7 on 2023-07-26 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_alter_feed_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='userProfile',
            new_name='user',
        ),
    ]
