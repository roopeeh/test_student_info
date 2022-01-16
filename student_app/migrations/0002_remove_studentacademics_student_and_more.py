# Generated by Django 4.0 on 2022-01-11 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentacademics',
            name='student',
        ),
        migrations.AddField(
            model_name='studentacademics',
            name='Student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='student_app.studentinfo'),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='Biology',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='Chemistry',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='English',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='Maths',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='Physics',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='Address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='Class',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='Name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='School',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='mobail',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
