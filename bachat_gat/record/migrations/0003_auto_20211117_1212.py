# Generated by Django 3.2.9 on 2021-11-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_alter_userdetails_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='availableAmount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='totalAmount',
            field=models.IntegerField(default=0),
        ),
    ]
