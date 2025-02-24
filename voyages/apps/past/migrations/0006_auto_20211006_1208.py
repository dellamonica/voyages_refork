# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2021-10-06 12:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('past', '0005_enslavedcontribution_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnslavedInRelation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EnslavementRelation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('relation_type', models.IntegerField()),
                ('date', models.CharField(help_text='Date in MM,DD,YYYY format with optional fields.', max_length=12, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('text_ref', models.CharField(blank=True, help_text='Source text reference', max_length=255)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='voyage.Place')),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='voyage.VoyageSources')),
                ('voyage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='voyage.Voyage')),
            ],
        ),
        migrations.CreateModel(
            name='EnslaverInRelation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('role', models.IntegerField(help_text='The role of the enslaver in this relation')),
                ('enslaver_alias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.EnslaverAlias')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.EnslavementRelation')),
            ],
        ),
        migrations.RenameField(
            model_name='enslaved',
            old_name='modern_name_first',
            new_name='modern_name',
        ),
        migrations.RemoveField(
            model_name='enslaved',
            name='is_adult',
        ),
        migrations.RemoveField(
            model_name='enslaved',
            name='modern_name_second',
        ),
        migrations.RemoveField(
            model_name='enslaved',
            name='modern_name_third',
        ),
        migrations.AddField(
            model_name='enslaved',
            name='captive_status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='dataset',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='last_known_date',
            field=models.CharField(blank=True, help_text='Date in format: MM,DD,YYYY', max_length=10, null=True, validators=[django.core.validators.RegexValidator(re.compile('^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$', 32), code='invalid', message='Please type a date in the format MM,DD,YYYY (individual entries may be blank)')]),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='notes',
            field=models.CharField(max_length=8192, null=True),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='skin_color',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='enslaved',
            name='height',
            field=models.FloatField(null=True, verbose_name='Height in inches'),
        ),
        migrations.AlterField(
            model_name='enslavedsourceconnection',
            name='enslaved',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='past.Enslaved'),
        ),
        migrations.AlterField(
            model_name='languagegroup',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Latitude of point'),
        ),
        migrations.AlterField(
            model_name='languagegroup',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Longitude of point'),
        ),
        migrations.AlterField(
            model_name='moderncountry',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Latitude of Country'),
        ),
        migrations.AlterField(
            model_name='moderncountry',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Longitude of Country'),
        ),
        migrations.AddField(
            model_name='enslavedinrelation',
            name='enslaved',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.Enslaved'),
        ),
        migrations.AddField(
            model_name='enslavedinrelation',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.EnslavementRelation'),
        ),
    ]
