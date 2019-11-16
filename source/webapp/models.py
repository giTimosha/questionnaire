from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


RATING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

CATEGORY_CHOICES = (
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('household', 'Товары для дома'),
)


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товар')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        permissions = [
            ('can_have_piece_of_pizza', 'Может съесть кусочек пиццы'),
        ]


class Review(models.Model):
    author = models.ForeignKey(User, related_name= 'users', on_delete=models.CASCADE, verbose_name='автор')
    product = models.ForeignKey('webapp.Product', related_name='products', on_delete=models.CASCADE,
                                verbose_name='товар')
    review = models.TextField(max_length=600, verbose_name='текст отзыва')
    assessment = models.CharField(max_length=1, choices=RATING_CHOICES, verbose_name='оценка')

    def __str__(self):
        return '{} -- {}' .format(self.author, self.product)

