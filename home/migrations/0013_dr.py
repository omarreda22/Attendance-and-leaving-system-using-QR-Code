# Generated by Django 4.0.4 on 2022-05-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_login_id_attendance_list_loginid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Drs',
            },
        ),
    ]