# Generated by Django 3.2.7 on 2021-09-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0003_auto_20210911_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='identifiers',
            name='isbn_10',
            field=models.CharField(blank=True, max_length=124, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='identifiers',
            name='isbn_13',
            field=models.CharField(blank=True, max_length=124, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='identifiers',
            name='other',
            field=models.CharField(blank=True, max_length=124, null=True, unique=True),
        ),
    ]