# Generated by Django 4.1.2 on 2022-11-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0001_initial"),
        ("classes", "0002_class_schedule"),
    ]

    operations = [
        migrations.RenameField(
            model_name="class",
            old_name="capacity",
            new_name="max_capacity",
        ),
        migrations.AddField(
            model_name="class",
            name="customers",
            field=models.ManyToManyField(
                null=True, related_name="classes", to="customers.customer"
            ),
        ),
        migrations.AddField(
            model_name="class",
            name="vacancies",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]