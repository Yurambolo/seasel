# Generated by Django 3.2.8 on 2022-05-28 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_feedback_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='composition',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.composition'),
            preserve_default=False,
        ),
    ]