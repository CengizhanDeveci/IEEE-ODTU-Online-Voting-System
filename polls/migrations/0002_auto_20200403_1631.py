# Generated by Django 3.0.2 on 2020-04-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='altıncı',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='beşinci',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='birinci',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='dördüncü',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='ikinci',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='yedinci',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='üçüncü',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='imagename',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
