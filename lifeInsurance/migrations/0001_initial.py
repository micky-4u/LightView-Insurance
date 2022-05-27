# Generated by Django 4.0.3 on 2022-05-27 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('derivers_license', models.FileField(upload_to='doc/')),
                ('passport', models.FileField(upload_to='doc/')),
                ('adhaar', models.FileField(upload_to='doc/')),
                ('pan_card', models.FileField(upload_to='doc/')),
                ('salary_slip', models.FileField(upload_to='doc/')),
                ('bank_statement', models.FileField(upload_to='doc/')),
                ('itr', models.FileField(upload_to='doc/')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='client.client')),
            ],
        ),
    ]
