# Generated by Django 2.0 on 2020-11-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_previouspatient'),
    ]

    operations = [
        migrations.AddField(
            model_name='previouspatient',
            name='patientID',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]