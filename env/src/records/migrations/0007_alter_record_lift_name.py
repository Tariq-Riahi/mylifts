# Generated by Django 4.1.7 on 2023-03-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_alter_record_lift_name_alter_record_weight_lifted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='lift_name',
            field=models.CharField(choices=[('Bench press', 'Bench press'), ('Squat', 'Squat'), ('Deadlift', 'Deadlift'), ('Overhead Press', 'Overhead Press')], max_length=50),
        ),
    ]
