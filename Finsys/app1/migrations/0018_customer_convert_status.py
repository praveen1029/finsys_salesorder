# Generated by Django 4.2.3 on 2023-10-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0017_auto_20231019_0525"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="convert_status",
            field=models.IntegerField(default=0),
        ),
    ]
