# Generated by Django 5.1.4 on 2024-12-11 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_usertoken_max_attempt"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usertoken",
            old_name="expired_by",
            new_name="expired_at",
        ),
    ]