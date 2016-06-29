# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('cost', models.FloatField(blank=True)),
                ('is_in', models.BooleanField(default=True)),
                ('inventory', models.ForeignKey(to='inventory.Inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('stock_on_hand', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('contact', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='item',
            field=models.ForeignKey(to='inventory.Item'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='supplier',
            field=models.ForeignKey(to='inventory.Supplier'),
        ),
    ]
