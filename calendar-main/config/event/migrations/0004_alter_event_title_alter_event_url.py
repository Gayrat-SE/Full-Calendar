# Generated by Django 4.0.5 on 2022-06-28 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_alter_event_end_date_alter_event_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.URLField(),
        ),
    ]
