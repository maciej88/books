# Generated by Django 3.2.7 on 2021-09-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0006_auto_20210911_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=124, null=True, verbose_name='autor'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=124, null=True, verbose_name='Numer ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(null=True, verbose_name='Liczba stron'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_language',
            field=models.CharField(max_length=124, null=True, verbose_name='Język publikacji'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publshed_date',
            field=models.DateField(null=True, verbose_name='Data publikacji'),
        ),
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.URLField(null=True, verbose_name='Link do okładki'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=124, verbose_name='Tytuł'),
        ),
    ]
