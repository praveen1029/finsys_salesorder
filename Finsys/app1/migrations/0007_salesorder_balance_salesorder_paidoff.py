# Generated by Django 4.2.3 on 2023-10-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0006_rename_complete_status_salesorder_inv_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesorder",
            name="balance",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="salesorder",
            name="paidoff",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
