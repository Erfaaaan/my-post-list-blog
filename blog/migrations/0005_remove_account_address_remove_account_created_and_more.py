# Generated by Django 4.0 on 2022-03-04 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_account_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='address',
        ),
        migrations.RemoveField(
            model_name='account',
            name='created',
        ),
        migrations.RemoveField(
            model_name='account',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='account',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
    ]