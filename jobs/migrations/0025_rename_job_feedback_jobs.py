# Generated by Django 4.2.15 on 2024-09-11 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0024_remove_feedback_application_feedback_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='job',
            new_name='jobs',
        ),
    ]
