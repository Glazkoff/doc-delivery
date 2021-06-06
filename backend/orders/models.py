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
    WEIGHT_CHOICES = (('1', 'До 1 кг'), ('5', 'До 5 кг'), ('10', 'До 10 кг'),
                      ('15', 'До 15 кг'))
    PAYMENT_CHOICES = (('card', 'Картой онлайн'),
                       ('cash', 'Наличными курьеру'))
    TRANSPORT_CHOICES = (('onfoot', 'Пешком'),
                         ('oncar', 'На машине'))
    departure_date = models.DateField(verbose_name='Дата отправления')
    arrival_date = models.DateField(
        verbose_name='Дата доставки', null=True, blank=True)
    cost = models.IntegerField(verbose_name='Стоимость доставки, ₽')
    salary_part = models.IntegerField(verbose_name='Часть зарплаты курьера, ₽')
    courier = models.ForeignKey(
        Courier, verbose_name='Курьер', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        verbose_name='Статус заказа', max_length=1, choices=STATUS_CHOICES, default="0")
    weight = models.CharField(
        verbose_name='Вес заказа', max_length=2, choices=WEIGHT_CHOICES, default="1")
    parcel_value = models.IntegerField(
        verbose_name='Ценность посылки', null=True, blank=True)
    payment = models.CharField(
        verbose_name='Способ оплаты', max_length=4, choices=PAYMENT_CHOICES, default="cash")
    delivery_way = models.CharField(
        verbose_name='Как доставить', max_length=6, choices=TRANSPORT_CHOICES, default="oncar")
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
