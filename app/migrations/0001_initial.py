# Generated by Django 4.0.5 on 2022-06-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=255)),
                ('song_url', models.CharField(max_length=255)),
                ('song_image', models.ImageField(upload_to='')),
                ('song_data', models.FileField(upload_to='')),
                ('song_lyrics', models.TextField()),
                ('song_datetime', models.DateTimeField()),
            ],
        ),
    ]
