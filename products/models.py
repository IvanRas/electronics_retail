from django.db import models
from retail.models import Factory, Network, Entrepreneur


class BaseProduct(models.Model):
    prod_name = models.CharField(max_length=150, verbose_name='название продукта')
    model = models.CharField(max_length=150, verbose_name='модель')
    product_launch_date = models.DateTimeField(verbose_name='дата выхода на рынок')

    class Meta:
        abstract = True


class FactoryProduct(BaseProduct):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.prod_name}'

    class Meta:
        verbose_name = 'продукт завода'
        verbose_name_plural = 'продукты завода'


class NetworkProduct(BaseProduct):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.prod_name}'

    class Meta:
        verbose_name = 'продукт розничной сети'
        verbose_name_plural = 'продукты розничных сетей'


class EntrepreneurProduct(BaseProduct):
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.prod_name}'

    class Meta:
        verbose_name = 'продукт индивидуального предпринимателя'
        verbose_name_plural = 'продукты индивидуальных предпринимателей'