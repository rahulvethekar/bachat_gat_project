# Generated by Django 3.2.9 on 2021-11-16 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.username'),
        ),
    ]
