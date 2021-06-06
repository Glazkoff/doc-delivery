from django.db import models

# Create your models here.


class Courier(models.Model):
    name = models.CharField('Имя', max_length=100)

    class Meta:
        verbose_name = "Курьер"
        verbose_name_plural = "Курьеры"

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (('0', 'Поиск курьера'), ('1', 'Курьер движется к отправителю'), ('2', 'Курьер движется к получателю'),
                      ('3', 'Подтверждение личности получателя'), ('4', 'Передача посылки получателю'), ('5', 'Завершено'))
    departure_date = models.DateField(verbose_name='Дата отправления')
    arrival_date = models.DateField(
        verbose_name='Дата доставки', null=True, blank=True)
    cost = models.IntegerField(verbose_name='Стоимость доставки, ₽')
    salary_part = models.IntegerField(verbose_name='Часть зарплаты курьера, ₽')
    courier = models.ForeignKey(
        Courier, verbose_name='Курьер', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        verbose_name='Статус заказа', max_length=10, choices=STATUS_CHOICES, default="0")
    address_from = models.CharField(
        verbose_name='Адрес отправления', max_length=100)
    address_to = models.CharField(
        verbose_name='Адрес получения', max_length=100)
    sender = models.CharField(verbose_name='ФИО отправителя', max_length=100)
    recipient = models.CharField(
        verbose_name='ФИО получателя', max_length=100)
    pointFromLat = models.DecimalField(
        verbose_name='Широта точки отправителя', max_digits=10, decimal_places=8, null=True, blank=True)
    pointFromLng = models.DecimalField(
        verbose_name='Долгота точки отправителя', max_digits=10, decimal_places=8, null=True, blank=True)
    pointToLat = models.DecimalField(
        verbose_name='Широта точки получателя', max_digits=10, decimal_places=8, null=True, blank=True)
    pointToLng = models.DecimalField(
        verbose_name='Долгота точки получателя', max_digits=10, decimal_places=8, null=True, blank=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return "Заказ #" + str(self.id)
