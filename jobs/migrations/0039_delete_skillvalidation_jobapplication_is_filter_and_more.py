# Generated by Django 4.2.15 on 2024-10-30 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0038_delete_skillvalidation_quizresults_total'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='jobapplication',
            name='is_filter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='is_filter_applied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='reason',
            field=models.BooleanField(default=False),
        ),
    ]
