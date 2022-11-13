# Generated by Django 4.1.3 on 2022-11-12 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='time_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.TimeField()),
                ('Title', models.CharField(max_length=300, verbose_name='Title')),
                ('Description', models.TextField(verbose_name='Description')),
                ('Day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.days')),
            ],
        ),
    ]
