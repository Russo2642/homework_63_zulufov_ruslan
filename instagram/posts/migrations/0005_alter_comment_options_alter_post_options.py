# Generated by Django 4.1.7 on 2023-03-24 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment_created_at_comment_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
    ]