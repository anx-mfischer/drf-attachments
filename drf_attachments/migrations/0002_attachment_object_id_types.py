# Generated by Django 3.2.9 on 2021-11-23 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_attachments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='object_id',
            field=models.CharField(db_index=True, max_length=64),
        ),
    ]
