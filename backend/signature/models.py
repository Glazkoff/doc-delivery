from django.db import models

# Create your models here.


class Signature(models.Model):
    signature = models.TextField('Зашифрованная подпись')

    class Meta:
        verbose_name = "Подпись"
        verbose_name_plural = "Подписи"

    def __str__(self):
        return "Подпись #" + str(self.id)
