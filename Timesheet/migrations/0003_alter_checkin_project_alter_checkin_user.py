# Generated by Django 4.1.2 on 2022-11-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timesheet', '0002_alter_checkin_project_alter_checkin_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='project',
            field=models.CharField(default='admin', max_length=45),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='user',
            field=models.CharField(default='admin', max_length=45),
        ),
    ]
