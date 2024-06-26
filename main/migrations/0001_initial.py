# Generated by Django 5.0.6 on 2024-06-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('preview', models.CharField(max_length=250, verbose_name='Анонс')),
                ('content', models.TextField(verbose_name='Текст статьи')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
