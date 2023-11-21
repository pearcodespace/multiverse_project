# Generated by Django 4.1.10 on 2023-11-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_textsentiment", "0002_remove_text_api_result"),
    ]

    operations = [
        migrations.CreateModel(
            name="APIResponse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("result_key", models.CharField(max_length=255)),
                ("result_value", models.TextField()),
            ],
        ),
    ]