# Generated by Django 2.1.5 on 2019-01-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(max_length=100)),
                ('base', models.CharField(choices=[('chocolate', 'Chocolate'), ('vanilla', 'Vanilla')], default='Vanilla', max_length=100)),
                ('available', models.CharField(choices=[('cookies and creme', 'Cookies and Cream'), ('mooose tracks', 'Moose Tracks'), ('chocolate cherry', 'Chocolate Cherry')], default='Cookies and Creme', max_length=100)),
                ('featured', models.BooleanField()),
                ('date_churned', models.DateField()),
            ],
        ),
    ]
