# Generated by Django 4.1.7 on 2023-03-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Мужской'), ('FEMALE', 'Женский'), ('OTHER', 'Пол')], default='OTHER', max_length=7, verbose_name='Пол'),
        ),
    ]
