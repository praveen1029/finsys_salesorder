# Generated by Django 4.2.3 on 2023-10-31 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0010_salesorder_adjust"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="invoiceno",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="recinvoice",
            name="recinvoiceno",
            field=models.CharField(max_length=100),
        ),
    ]
