# Generated by Django 4.2.15 on 2024-10-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0041_delete_skillvalidation_jobpost_is_filter'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='jobapplication',
            name='hide',
            field=models.BooleanField(default=False),
        ),
    ]
