# Generated by Django 3.0.6 on 2020-06-21 10:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apsi_app', '0007_auto_20200613_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advert',
            old_name='user',
            new_name='creator',
        ),
        migrations.AddField(
            model_name='user',
            name='observed_adverts',
            field=models.ManyToManyField(blank=True, to='apsi_app.Advert'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='subscribing_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
