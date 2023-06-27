# Generated by Django 4.2 on 2023-06-18 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spell_name', models.CharField(max_length=200)),
                ('spell_desc', models.CharField(max_length=1000)),
                ('spell_dur', models.CharField(max_length=200)),
                ('spell_lvl', models.IntegerField(default=1)),
                ('spell_range', models.CharField(max_length=100)),
                ('spell_fave', models.BooleanField(default=False)),
            ],
        ),
    ]
