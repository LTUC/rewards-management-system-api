# Generated by Django 3.2.8 on 2021-11-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewads',
            name='reward',
            field=models.CharField(choices=[('Waive Late Assignment Penalty', 'Waive Late Assignment Penalty'), ('Resubmit attempt', 'Resubmit attempt'), ('Waive Late of class penalty', 'Waive Late of class penalty'), ('+1 mark on any submission', '+1 mark on any submission')], max_length=80),
        ),
    ]
