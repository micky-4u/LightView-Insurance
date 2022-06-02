# Generated by Django 4.0.3 on 2022-06-02 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('client_code', models.IntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('national_id', models.CharField(max_length=100)),
                ('id_number', models.PositiveIntegerField()),
                ('tin', models.PositiveIntegerField()),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='agent.agent')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
