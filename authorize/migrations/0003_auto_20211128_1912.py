# Generated by Django 3.2.8 on 2021-11-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorize', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('ADMIN', 'ADMIN'), ('TEACHER', 'TEACHER'), ('STUDENT', 'STUDENT')], max_length=10, null=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='music_school',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='music_school',
        ),
        migrations.DeleteModel(
            name='Administrator',
        ),
    ]
