# Generated by Django 4.0 on 2022-03-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_account_address_account_created_account_sex_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
