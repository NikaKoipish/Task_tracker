# Generated by Django 5.0.7 on 2024-07-20 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="comments",
            field=models.TextField(
                blank=True, null=True, verbose_name="Комментарии к задаче"
            ),
        ),
    ]
