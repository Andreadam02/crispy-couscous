# Generated by Django 4.2.5 on 2023-09-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploaded_files/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
