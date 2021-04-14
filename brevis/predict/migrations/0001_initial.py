# Generated by Django 3.2 on 2021-04-14 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('body_summarized', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('text_len', models.PositiveIntegerField(blank=True, null=True)),
                ('summary_len', models.PositiveIntegerField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
