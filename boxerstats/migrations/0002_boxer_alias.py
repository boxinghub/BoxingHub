# Generated by Django 5.2 on 2025-04-28 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxerstats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxer',
            name='alias',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
