# Generated by Django 3.2.9 on 2021-11-16 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalAmount', models.IntegerField()),
                ('availableAmount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MonthName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saving', models.IntegerField(default=0)),
                ('intrest', models.IntegerField(default=0)),
                ('loan', models.IntegerField(default=0)),
                ('paidLoan', models.IntegerField(default=0)),
                ('borrowLoan', models.IntegerField(default=0)),
                ('fine', models.IntegerField(default=0)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.monthname')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='record.username')),
            ],
        ),
    ]
