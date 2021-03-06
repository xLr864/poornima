# Generated by Django 3.2.9 on 2022-02-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_app', '0003_career'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career',
            old_name='branch',
            new_name='ugbranch',
        ),
        migrations.RenameField(
            model_name='career',
            old_name='areaofexp',
            new_name='ugcity',
        ),
        migrations.RenameField(
            model_name='career',
            old_name='college',
            new_name='ugcollege',
        ),
        migrations.RenameField(
            model_name='career',
            old_name='passing_year',
            new_name='ugpassing_year',
        ),
        migrations.RenameField(
            model_name='career',
            old_name='percentage',
            new_name='ugpercentage',
        ),
        migrations.RenameField(
            model_name='career',
            old_name='thesis_title',
            new_name='uguniversity',
        ),
        migrations.RemoveField(
            model_name='career',
            name='status',
        ),
        migrations.RemoveField(
            model_name='career',
            name='university',
        ),
        migrations.AddField(
            model_name='career',
            name='docareaofexp',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='doccity',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='doccollege',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='docpassing_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='docstatus',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='docthesis_title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='docuniversity',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='pgareaofexp',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='pgcity',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='pgcollege',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='pgpassing_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='pgpercentage',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='pgthesis_title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='pguniversity',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='designation',
            field=models.CharField(max_length=50),
        ),
    ]
