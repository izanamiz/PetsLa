# Generated by Django 3.2 on 2021-11-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211114_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.TextField(max_length=500, null=True),
        ),
    ]