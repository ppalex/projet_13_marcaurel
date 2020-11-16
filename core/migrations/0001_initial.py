# Generated by Django 3.1.2 on 2020-11-15 17:13

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
                ('region', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(choices=[('pending', 'En attente'), ('accepted', 'Accepté'), ('refused', 'Refusé')], max_length=255)),
                ('invitation_date', models.DateTimeField()),
                ('response_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
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
            ],
        ),
        migrations.CreateModel(
            name='MatchRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(choices=[('pending', 'En attente'), ('accepted', 'Accepté'), ('refused', 'Refusé')], max_length=255)),
                ('request_date', models.DateTimeField()),
                ('response_date', models.DateTimeField(blank=True, null=True)),
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
                ('player_subscriptions', models.ManyToManyField(blank=True, to='core.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(choices=[('keeper', 'Gardien'), ('defensive', 'Défenseur'), ('forward', 'Attaquant'), ('center', 'Milieu')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField(blank=True, null=True)),
                ('invitation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.invitation')),
                ('match', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.match')),
                ('match_request', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.matchrequest')),
                ('player', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='positions',
            field=models.ManyToManyField(to='core.Position'),
        ),
    ]
