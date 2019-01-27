# Generated by Django 2.1.5 on 2019-01-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('games', models.IntegerField()),
                ('score', models.IntegerField()),
                ('win', models.IntegerField()),
                ('equal', models.IntegerField()),
                ('lose', models.IntegerField()),
                ('goal_achived', models.IntegerField()),
                ('goal', models.IntegerField()),
                ('dif_goal', models.IntegerField()),
            ],
        ),
    ]
