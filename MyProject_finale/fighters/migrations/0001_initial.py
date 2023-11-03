# Generated by Django 4.2.5 on 2023-09-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immagine', models.ImageField(upload_to='')),
                ('nome', models.CharField(max_length=20)),
                ('descrizione', models.CharField(max_length=40)),
            ],
        ),
    ]