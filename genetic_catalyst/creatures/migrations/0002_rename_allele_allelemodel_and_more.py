# Generated by Django 4.2.5 on 2023-09-26 01:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("creatures", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Allele",
            new_name="AlleleModel",
        ),
        migrations.RenameModel(
            old_name="Attribute",
            new_name="AttributeModel",
        ),
        migrations.RenameModel(
            old_name="Creature",
            new_name="CreatureModel",
        ),
        migrations.RenameModel(
            old_name="Gene",
            new_name="GeneModel",
        ),
    ]
