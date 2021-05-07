# Generated by Django 3.1.7 on 2021-04-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convo', models.CharField(max_length=10)),
                ('sender', models.IntegerField()),
                ('msg', models.TextField(max_length=200)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]