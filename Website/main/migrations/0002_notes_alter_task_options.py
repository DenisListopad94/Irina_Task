# Generated by Django 4.1.3 on 2022-12-04 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('full_text', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Дата записи')),
            ],
            options={
                'verbose_name': ('Заметка',),
                'verbose_name_plural': 'Заметки',
            },
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': ('Задача',), 'verbose_name_plural': 'Задачи'},
        ),
    ]
