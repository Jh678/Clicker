# Generated by Django 4.0.3 on 2022-06-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_boost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='core',
            old_name='click_power',
            new_name='clikc_power',
        ),
        migrations.AddField(
            model_name='core',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='boost',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
