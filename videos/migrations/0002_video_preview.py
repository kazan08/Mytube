# Generated by Django 5.1.2 on 2024-10-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='preview',
            field=models.ImageField(null=True, upload_to='previews/%Y/%m/%d/', verbose_name='Превью'),
        ),
    ]
