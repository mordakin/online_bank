from django.db import models


class Users(models.Model):
    FIO = models.CharField(max_length=255, verbose_name='ФИО')
    phone_number = models.IntegerField(unique=True, verbose_name='Номер телефона')
    card_number = models.BigIntegerField(unique=True, verbose_name='Номер карты')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    amount_of_funds = models.IntegerField(default=0, verbose_name='Количество средств')

