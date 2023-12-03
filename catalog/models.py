from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='previews/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price_for_one = models.IntegerField(verbose_name='цена за штуку', **NULLABLE)
    date_of_creation = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    last_modified_date = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    def price(self):
        return f'{self.price_for_one} руб.'

    def info(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'
