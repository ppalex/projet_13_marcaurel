# Generated by Django 3.1.2 on 2020-11-08 08:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('region', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinate', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('sex', models.CharField(choices=[('masculine', 'M'), ('feminine', 'F')], max_length=10)),
                ('level', models.CharField(choices=[('novice', 'Débutant'), ('intermediate', 'Intermédiaire'), ('advanced', 'Avancé')], max_length=50)),
                ('address', models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='core.address')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='core.location')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(choices=[('public', 'Public'), ('private', 'Privé')], max_length=255)),
                ('fixture', models.DateTimeField()),
                ('num_player', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('full', models.BooleanField()),
                ('started', models.BooleanField()),
                ('cancelled', models.BooleanField()),
                ('over', models.BooleanField()),
                ('address', models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='core.address')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='core.location')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(choices=[('pending', 'En attente'), ('accepted', 'Accepté'), ('refused', 'Refusé')], max_length=255)),
                ('invitation_date', models.DateTimeField()),
                ('response_date', models.DateTimeField(blank=True, null=True)),
                ('by_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.player')),
                ('for_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.player')),
            ],
        ),
    ]
