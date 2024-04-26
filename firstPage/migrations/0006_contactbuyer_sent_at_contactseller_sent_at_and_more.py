# Generated by Django 5.0.4 on 2024-04-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0005_contactbuyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactbuyer',
            name='sent_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contactseller',
            name='sent_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='approved_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='requested_product',
            name='requested_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]