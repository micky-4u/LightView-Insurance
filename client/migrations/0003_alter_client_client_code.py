# Generated by Django 4.0.3 on 2022-06-02 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_client_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_code',
            field=models.IntegerField(auto_created=True, blank=True, default=48658624640054),
        ),
    ]
