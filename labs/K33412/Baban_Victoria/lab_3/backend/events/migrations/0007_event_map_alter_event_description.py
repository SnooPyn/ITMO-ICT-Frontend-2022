# Generated by Django 4.1.5 on 2023-01-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0006_event_contact_name_event_contact_number_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="map",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]