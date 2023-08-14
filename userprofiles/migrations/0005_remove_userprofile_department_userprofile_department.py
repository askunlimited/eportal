# Generated by Django 4.2.4 on 2023-08-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0004_alter_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='department',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.ManyToManyField(blank=True, default=1, related_name='user_department', to='userprofiles.department'),
        ),
    ]
