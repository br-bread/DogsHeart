# Generated by Django 3.2.18 on 2023-04-23 09:13

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
                ('name', models.TextField(help_text='Максимальная длина 40 символов', max_length=40, verbose_name='название')),
                ('is_breed', models.BooleanField(default=False, verbose_name='статья о породе')),
                ('description', models.TextField(help_text='Максимальная длина 100 символов', max_length=100, verbose_name='краткое описание')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('text', models.TextField(help_text='Содержание статьи', verbose_name='статья')),
            ],
        ),
    ]
