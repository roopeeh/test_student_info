# Generated by Django 4.0 on 2022-01-16 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_alter_studentinfo_roll_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='mobail',
            new_name='mobile',
        ),
    ]
