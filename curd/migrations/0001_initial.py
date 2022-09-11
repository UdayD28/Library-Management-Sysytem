# Generated by Django 4.1.1 on 2022-09-10 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("book_name", models.CharField(max_length=100)),
                ("book_description", models.TextField(blank=True)),
                ("year_published", models.DateField(blank=True)),
                ("created_date", models.DateTimeField(blank=True)),
                ("author", models.CharField(blank=True, max_length=60)),
                ("publish", models.BooleanField(default=True)),
            ],
        ),
    ]