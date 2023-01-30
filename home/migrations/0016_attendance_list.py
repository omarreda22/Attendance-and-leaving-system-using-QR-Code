# Generated by Django 4.0.4 on 2022-05-21 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0015_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginid', models.CharField(blank=True, max_length=100)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.dr')),
                ('qrcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.attendance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Attendance List',
            },
        ),
    ]