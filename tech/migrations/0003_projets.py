# Generated by Django 4.2.2 on 2024-07-08 14:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tech", "0002_alter_blogs_description_alter_blogs_title_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projets",
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
                ("title", models.CharField(max_length=5000)),
                ("description", ckeditor.fields.RichTextField()),
                ("lin", models.CharField(max_length=500)),
                ("image", models.ImageField(upload_to="")),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]