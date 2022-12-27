# Generated by Django 3.2.16 on 2022-12-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assembly',
            name='title',
        ),
        migrations.AddField(
            model_name='assembly',
            name='title_of_activity',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='assembly',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]