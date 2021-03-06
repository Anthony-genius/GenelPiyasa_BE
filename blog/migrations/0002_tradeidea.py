# Generated by Django 3.0.2 on 2020-02-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeIdea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_subject', models.CharField(max_length=300)),
                ('trade_category', models.CharField(max_length=300)),
                ('trade_author', models.CharField(max_length=300)),
                ('trade_published', models.DateTimeField(auto_now_add=True)),
                ('trade_content', models.TextField()),
                ('trade_status_flag', models.CharField(default='waiting', max_length=300)),
                ('trade_score', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
