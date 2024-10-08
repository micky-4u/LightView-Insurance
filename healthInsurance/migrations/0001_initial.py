# Generated by Django 4.0.3 on 2022-06-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_form', models.FileField(upload_to='doc/')),
                ('statementOfHealth_form', models.FileField(upload_to='doc/')),
                ('birth_certificate', models.FileField(upload_to='doc/')),
                ('passport', models.FileField(upload_to='doc/')),
                ('voting_id_copy', models.FileField(upload_to='doc/')),
                ('voting_id', models.IntegerField()),
                ('driving_license', models.FileField(upload_to='doc/')),
                ('electricity_bill', models.FileField(upload_to='doc/')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_form', models.FileField(upload_to='doc/')),
                ('discharge_card', models.FileField(upload_to='doc/')),
                ('doctors_report', models.FileField(upload_to='doc/')),
                ('hospital_bill', models.FileField(upload_to='doc/')),
                ('x_ray_film', models.FileField(upload_to='doc/')),
                ('other_documents', models.FileField(upload_to='doc/')),
            ],
        ),
    ]
