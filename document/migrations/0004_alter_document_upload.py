# Generated by Django 4.2.4 on 2023-08-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_alter_document_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='upload',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]
