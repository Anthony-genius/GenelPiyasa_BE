# Generated by Django 3.0.2 on 2020-02-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_exam_exam_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='exam_limit_count',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_limit_time',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
    ]
