# Generated by Django 3.0.7 on 2023-06-12 09:17

import apps.arena.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('mode_start', models.TimeField()),
                ('mode_end', models.TimeField()),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('price_hour', models.FloatField()),
                ('min_pre_hour', models.FloatField()),
                ('fine_refuse_price', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='arena/default.png', upload_to=apps.arena.models.get_image)),
                ('arena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena.Arena')),
            ],
        ),
    ]
