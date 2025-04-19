from django.db import models


class BaseRetail(models.Model):
    name = models.CharField(max_length=350, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house_number = models.CharField(max_length=50, verbose_name='номер дома')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='задолженность')
    time_created = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

    class Meta:
        abstract = True


class Factory(BaseRetail):
    """завод"""

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'


class Network(BaseRetail):
    """розничная сеть"""

    supplier = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='поставщик')

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'


class Entrepreneur(BaseRetail):
    """индивидуальный предприниматель"""

    supplier = models.ForeignKey(Network, on_delete=models.CASCADE, verbose_name='поставщик')

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'индивидуальный предприниматель'
        verbose_name_plural = 'индивидуальные предприниматели'
