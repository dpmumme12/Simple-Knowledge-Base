# Generated by Django 4.0.2 on 2022-05-15 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='conversation_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
