# Generated by Django 4.2.15 on 2024-09-12 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0028_remove_profile_verification_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnumber', models.CharField(max_length=13, unique=True)),
                ('phone', models.CharField(default=' ', max_length=10, null=True)),
                ('dob', models.CharField(max_length=6)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.CharField(max_length=6)),
                ('maritial_status', models.CharField(default=' ', max_length=10)),
                ('race', models.CharField(default=' ', max_length=15)),
                ('disability', models.CharField(default=' ', max_length=30)),
                ('is_verified', models.BooleanField(default=False)),
                ('linkedin_profile', models.CharField(default=' ', max_length=225)),
                ('personal_website', models.CharField(default=' ', max_length=225)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
