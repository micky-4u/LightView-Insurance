# Generated by Django 4.0.3 on 2022-06-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0003_policytype_policy_code_alter_offers_offer_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='offer_code',
            field=models.IntegerField(auto_created=True, blank=True, default=138734403303733678, max_length=100),
        ),
        migrations.AlterField(
            model_name='policytype',
            name='policy_code',
            field=models.IntegerField(auto_created=True, blank=True, default=48658624640054, max_length=100),
        ),
    ]
