# Generated by Django 4.2.2 on 2024-10-23 13:23

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):
    dependencies = [
        ("tech", "0011_equipe"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogs",
            name="description",
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
        migrations.AlterField(
            model_name="services",
            name="description",
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
