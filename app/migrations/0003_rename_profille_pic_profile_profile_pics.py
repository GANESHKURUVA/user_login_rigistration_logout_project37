# Generated by Django 4.2 on 2023-05-05 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_profile_profille_pic"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="profille_pic",
            new_name="profile_pics",
        ),
    ]