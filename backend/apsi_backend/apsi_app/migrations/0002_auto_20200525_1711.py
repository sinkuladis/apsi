# Generated by Django 3.0.6 on 2020-05-25 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apsi_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertmessage',
            old_name='advert',
            new_name='advert_id',
        ),
    ]
