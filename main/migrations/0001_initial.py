# Generated by Django 3.2.8 on 2021-10-26 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=40)),
                ('reward', models.CharField(choices=[('Waive Late Assignment Penalty', 'Waive Late Assignment Penalty'), ('Resubmit attempt', 'Resubmit attempt'), ('Waive Late of class penalty', 'Waive Late of class penalty'), ('+1 mark on any submission', '+1 mark on any submission')], max_length=80)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
