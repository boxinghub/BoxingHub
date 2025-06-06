# Generated by Django 5.2 on 2025-04-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxerstats', '0002_boxer_alias'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boxer',
            old_name='height_cm',
            new_name='height_metric',
        ),
        migrations.RenameField(
            model_name='boxer',
            old_name='reach_cm',
            new_name='reach_metric',
        ),
        migrations.AddField(
            model_name='boxer',
            name='height_imperial',
            field=models.CharField(default='', editable=False, max_length=10),
        ),
        migrations.AddField(
            model_name='boxer',
            name='reach_imperial',
            field=models.CharField(default='', editable=False, max_length=6),
        ),
    ]
