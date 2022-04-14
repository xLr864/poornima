# Generated by Django 3.2.9 on 2022-04-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_app', '0004_auto_20220219_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='career',
            name='docpassing_year',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='docstatus',
            field=models.CharField(default='NA', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='pgpassing_year',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='pgpercentage',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='ugpassing_year',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='ugpercentage',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
