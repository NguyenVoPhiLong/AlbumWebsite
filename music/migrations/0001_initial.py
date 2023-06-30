# Generated by Django 3.0.7 on 2020-06-26 12:30

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
            name='Album',
            fields=[
                ('albumid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('logo', models.CharField(blank=True, max_length=250, null=True)),
                ('star', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('songid', models.AutoField(primary_key=True, serialize=False)),
                ('songname', models.CharField(blank=True, max_length=250, null=True)),
                ('audio', models.CharField(blank=True, max_length=250, null=True)),
                ('star', models.CharField(blank=True, max_length=250, null=True)),
                ('albumid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='music.Album')),
            ],
        ),
    ]
