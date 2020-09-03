# Generated by Django 3.0.2 on 2020-05-28 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20200527_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_img',
        ),
        migrations.AddField(
            model_name='course',
            name='course_imglink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='svg_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='svg_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_img',
            field=models.URLField(blank=True, null=True),
        ),
    ]