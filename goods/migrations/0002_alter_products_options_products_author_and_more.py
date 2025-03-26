# Generated by Django 5.1.6 on 2025-03-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AddField(
            model_name='products',
            name='author',
            field=models.CharField(default='Unknown Author', max_length=255, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='products',
            name='publication_date',
            field=models.DateField(default='Unknown Date', verbose_name='Publication Date'),
        ),
        migrations.AddField(
            model_name='products',
            name='publisher',
            field=models.CharField(default='Unknown Publisher', max_length=255, verbose_name='Publisher'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Book Cover'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Book Title'),
        ),
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantity Available'),
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
    ]
