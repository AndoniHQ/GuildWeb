# Generated by Django 2.2.4 on 2020-05-28 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200529_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='clas',
            name='Character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Character'),
        ),
    ]
