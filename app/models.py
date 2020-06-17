from django.db import models


class Material(models.Model):
    """部品モデル"""
    code = models.CharField('コード', max_length=15)
    name = models.CharField('部品名', max_length=50)

    def __str__(self):
        return self.name


class Stock(models.Model):
    """在庫モデル"""
    code = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField('在庫数')


class Order(models.Model):
    """注文モデル"""
    code = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField('注文数')
