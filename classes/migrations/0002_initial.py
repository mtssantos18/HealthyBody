# Generated by Django 4.1.2 on 2022-11-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("customers", "0001_initial"),
        ("classes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="class",
            name="customers",
            field=models.ManyToManyField(
                related_name="classes", to="customers.customer"
            ),
        ),
    ]