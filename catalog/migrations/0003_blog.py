# Generated by Django 4.2.7 on 2023-12-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_last_modified_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='заголовок')),
                ('slug', models.CharField()),
                ('content', models.CharField(verbose_name='содержимое')),
                ('preview', models.ImageField(upload_to='blog_previews/', verbose_name='превью')),
                ('date_of_creation', models.DateTimeField(verbose_name='дата создания')),
                ('published', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('count_views', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
