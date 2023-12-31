# Generated by Django 4.2.3 on 2023-10-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0004_paymentterms_cid"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesorder",
            name="cheque_no",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="salesorder",
            name="complete_status",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="salesorder",
            name="pay_method",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="salesorder",
            name="upi_no",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
