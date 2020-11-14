# Generated by Django 2.0 on 2020-11-14 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare_workers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalMedicalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heartrate', models.IntegerField(blank=True, null=True)),
                ('sys_bp', models.IntegerField(blank=True, null=True)),
                ('dia_bp', models.IntegerField(blank=True, null=True)),
                ('body_temp', models.FloatField(blank=True, null=True)),
                ('oxygen_level', models.FloatField(blank=True, null=True)),
                ('breathing_rate', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateField()),
                ('bed', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='healthcare_workers.Bed')),
            ],
        ),
        migrations.CreateModel(
            name='RecentMedicalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heartrate', models.IntegerField(blank=True, null=True)),
                ('sys_bp', models.IntegerField(blank=True, null=True)),
                ('dia_bp', models.IntegerField(blank=True, null=True)),
                ('body_temp', models.FloatField(blank=True, null=True)),
                ('oxygen_level', models.FloatField(blank=True, null=True)),
                ('breathing_rate', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateField()),
                ('bed', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='healthcare_workers.Bed')),
            ],
        ),
    ]