# Generated by Django 4.2.3 on 2023-10-21 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_paymentterms"),
    ]

    operations = [
        migrations.RemoveField(model_name="paymentterms", name="cid",),
    ]
