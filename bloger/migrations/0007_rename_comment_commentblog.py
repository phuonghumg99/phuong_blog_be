# Generated by Django 3.2.9 on 2021-12-12 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloger', '0006_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='CommentBlog',
        ),
    ]
