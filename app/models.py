from django.db import models


class Stock(models.Model):
    """在庫モデル"""
    code = models.CharField('コード', max_length=20)
    quantity = models.IntegerField('在庫数')

    def __str__(self):
        return f'{self.code} / {self.quantity}'


class Order(models.Model):
    """注文モデル"""
    code = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField('注文数')
    remarks = models.CharField('備考', max_length=200, blank=True)
