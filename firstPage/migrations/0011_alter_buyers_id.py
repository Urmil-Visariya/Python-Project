# Generated by Django 5.0.2 on 2024-04-21 03:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0010_alter_buyers_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyers',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
