# Generated by Django 5.0 on 2024-01-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("first_name", models.CharField(max_length=55)),
                ("last_name", models.CharField(max_length=55)),
                ("username", models.CharField(max_length=55, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone_number", models.CharField(blank=True, max_length=20)),
                (
                    "role",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        choices=[(1, "Restaurant"), (2, "Customer")],
                        default=2,
                        null=True,
                    ),
                ),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("last_login", models.DateTimeField(auto_now_add=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]