# Generated by Django 3.0.7 on 2023-06-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arena', '0002_arena_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arena',
            name='fine_refuse_price',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='arena',
            name='min_pre_hour',
            field=models.FloatField(default=0, null=True),
        ),
    ]
