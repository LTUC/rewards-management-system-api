# Generated by Django 3.2.8 on 2021-10-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_rewads_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewads',
            name='reward',
            field=models.CharField(choices=[('Waive Late Assignment Penalty', 'Waive Late Assignment Penalty'), ('+1 mark on any submission', '+1 mark on any submission'), ('Waive Late of class penalty', 'Waive Late of class penalty'), ('Resubmit attempt', 'Resubmit attempt')], max_length=80),
        ),
    ]
