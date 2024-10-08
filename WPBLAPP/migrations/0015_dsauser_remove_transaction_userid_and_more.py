# Generated by Django 4.2.1 on 2023-09-06 11:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("WPBLAPP", "0014_remove_user_id_alter_user_num"),
    ]

    operations = [
        migrations.CreateModel(
            name="DSAUser",
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
                ("num", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=10)),
                (
                    "totalamount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("date", models.DateField(default=datetime.date.today)),
                ("year", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(model_name="transaction", name="userid",),
        migrations.AddField(
            model_name="transaction",
            name="usernum",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(name="User",),
    ]
