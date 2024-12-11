# Generated by Django 4.2.15 on 2024-09-21 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_industry'),
        ('jobs', '0028_jobpost_is_active_alter_jobpost_industry_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_required', models.BooleanField(default=False)),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='C_skills', to='jobs.jobpost')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.computerproficiency')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.computerskillslist')),
            ],
        ),
        migrations.CreateModel(
            name='SoftSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_required', models.BooleanField(default=False)),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='S_skills', to='jobs.jobpost')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.softproficiency')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.softskillslist')),
            ],
        ),
        migrations.RemoveField(
            model_name='academic',
            name='level',
        ),
        migrations.RemoveField(
            model_name='academic',
            name='qualification',
        ),
        migrations.AddField(
            model_name='academic',
            name='field_of_study',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='config.qualification'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='academic',
            name='nqf_level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='config.nqf'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
