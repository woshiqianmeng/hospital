# Generated by Django 4.0.3 on 2022-04-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_rename_ill_type_appointmentrecord_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentrecord',
            name='handled',
            field=models.BooleanField(default=False),
        ),
    ]
