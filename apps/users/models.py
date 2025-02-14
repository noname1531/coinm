from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефоный номер ",
    )
    age = models.IntegerField(
        verbose_name="Возраст",
        blank=True, null=True
    )
    direction = models.CharField(
        max_length=255,
        verbose_name="Направление",
    )
    balance = models.PositiveIntegerField(
        verbose_name="Баланс",
        default=4,
    )
    wallet = models.ImageField(
        verbose_name="Кошелек",
        default=0,
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.username} - {self.balance}'
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"