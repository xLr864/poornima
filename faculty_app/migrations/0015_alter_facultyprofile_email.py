# Generated by Django 3.2.9 on 2022-04-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_app', '0014_auto_20220414_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyprofile',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
