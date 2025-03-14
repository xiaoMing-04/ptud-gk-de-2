# Generated by Django 5.0 on 2025-03-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_task_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finished',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('I', 'In Progress'), ('C', 'Completed'), ('O', 'Overdue')], default='P', max_length=1),
        ),
    ]
