# Generated by Django 2.0.3 on 2018-11-23 21:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0004_job_hypervisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pruned',
            field=models.BooleanField(default=False),
        ),
    ]
