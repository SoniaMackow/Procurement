from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class TheContractor(models.Model):
    name = models.CharField(max_length=228)
    number_NIP = models.CharField(max_length=10, null=True)
    nameStreet = models.CharField(max_length=128)
    city = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} -  {self.nameStreet}  - {self.city}  - {self.number_NIP}  - {self.nameStreet} - {self.city}"


class Contract(models.Model):
    title = models.CharField(max_length=458)
    contractor = models.ManyToManyField('TheContractor')
    value_contract = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return f'{self.title} {self.contractor}'
    def get_absolute_url(self):
        return reverse('detail_contract', args=(self.id,))
class TypeProcurement(models.Model):
    type_procurement = models.CharField(max_length=258)
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.type_procurement} -  {self.contract}"


class Procedure(models.Model):
    name_procedure = models.CharField(max_length=558)
    data_initiation = models.DateField()
    value = models.DecimalField(max_digits=15, decimal_places=2)
    end_date_procedure = models.DateField()

    def __str__(self):
        return f"{self.name_procedure}-- {self.data_initiation} ---{self.value}--{self.end_date_procedure} "


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} {self.author} {self.contract} {self.date}"
