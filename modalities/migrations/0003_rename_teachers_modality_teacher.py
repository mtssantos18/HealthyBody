# Generated by Django 4.1.2 on 2022-11-02 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("modalities", "0002_modality_teachers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="modality",
            old_name="teachers",
            new_name="teacher",
        ),
    ]
