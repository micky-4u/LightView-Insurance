# Generated by Django 4.0.3 on 2022-04-27 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('policies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_category',
        ),
        migrations.CreateModel(
            name='MotoInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_of_driving', models.IntegerField(max_length=4)),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('insuranceForm', models.FileField(upload_to='doc/')),
                ('RC_Bood', models.FileField(upload_to='doc/')),
                ('identityProof', models.FileField(upload_to='doc/')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]
