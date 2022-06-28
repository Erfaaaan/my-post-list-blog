# Generated by Django 4.0 on 2022-03-04 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0002_account_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='sex',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6),
        ),
        migrations.AddField(
            model_name='account',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
