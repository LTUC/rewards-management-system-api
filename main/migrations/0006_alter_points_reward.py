# Generated by Django 3.2.8 on 2021-10-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_points_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='reward',
            field=models.CharField(choices=[('+1 mark on any submission', '+1 mark on any submission'), ('Waive Late Assignment Penalty', 'Waive Late Assignment Penalty'), ('Resubmit attempt', 'Resubmit attempt'), ('Waive Late of class penalty', 'Waive Late of class penalty')], max_length=80),
        ),
    ]
