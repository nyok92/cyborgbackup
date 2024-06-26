# Generated by Django 2.2.23 on 2021-05-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0014_fix_clientport_validation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('job', 'Default Backup Job'), ('check', 'Prepare Client or Repository'),
                                            ('catalog', 'Catalog Job'), ('prune', 'Prune Job'),
                                            ('restore', 'Restore Job'), ('integrity', 'Integrity Check Job')],
                                   default='job', max_length=64),
        ),
    ]
