# Generated by Django 3.2.8 on 2022-05-09 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
