# Generated by Django 4.2 on 2023-06-18 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spell',
            old_name='spell_desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='spell',
            old_name='spell_dur',
            new_name='duration',
        ),
        migrations.RenameField(
            model_name='spell',
            old_name='spell_fave',
            new_name='fave',
        ),
        migrations.RenameField(
            model_name='spell',
            old_name='spell_lvl',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='spell',
            old_name='spell_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='spell',
            old_name='spell_range',
            new_name='range',
        ),
    ]
