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


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, unique=True, verbose_name='Ссылка', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(default='479679246.jpg', upload_to='blogs/', verbose_name='Изображение', **NULLABLE)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', **NULLABLE)
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано', **NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров', **NULLABLE)

    def __str__(self):
        return f'{self.title}, {self.slug}'

    class Meta:
        verbose_name = 'статья'  # Настройка для наименования одного объекта
        verbose_name_plural = 'статьи'
