# Generated by Django 2.2.4 on 2020-05-30 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20200530_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='id',
        ),
        migrations.AddField(
            model_name='token',
            name='Region',
            field=models.CharField(choices=[('EU', 'EUROPA'), ('US', 'AMERICA')], default='EU', max_length=2, primary_key=True, serialize=False),
        ),
    ]
